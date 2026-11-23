
import asyncio
import json
from pathlib import Path
from datetime import datetime

from bleak import BleakScanner
from bleak.uuids import uuidstr_to_str
from mac_vendor_lookup import AsyncMacLookup
from winrt.windows.devices.bluetooth import BluetoothAddressType


devices = {}

HISTORY_FILE = Path("data/devices_history.json")


def current_time():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def classify_address_type(address_type):
    types = {
        BluetoothAddressType.PUBLIC: "Public",
        BluetoothAddressType.RANDOM: "Random",
        BluetoothAddressType.UNSPECIFIED: "Unspecified"
    }

    return types.get(address_type, "Desconhecido")


def classify_random_address(address):
    first_byte = int(address.split(":")[0], 16)
    address_bits = (first_byte >> 6) & 0b11

    types = {
        0b00: "Non-resolvable Private (NRPA)",
        0b01: "Resolvable Private (RPA)",
        0b10: "Reservado",
        0b11: "Static Random"
    }

    return types[address_bits]


def classify_signal(rssi):
    if rssi is None:
        return "Desconhecido"
    elif rssi >= -60:
        return "Excelente"
    elif rssi >= -70:
        return "Bom"
    elif rssi >= -85:
        return "Fraco"
    else:
        return "Muito fraco"


def identify_services(service_uuids):
    identified = []

    for uuid in service_uuids:
        name = uuidstr_to_str(uuid)

        identified.append({
            "uuid": uuid,
            "name": name
        })

    return identified


def callback(device, advertisement_data):
    address = device.address

    service_uuids = advertisement_data.service_uuids or []

    platform_data = advertisement_data.platform_data
    raw_data = platform_data[1]

    adv_type = classify_address_type(
        raw_data.adv.bluetooth_address_type
    )

    random_type = (
        classify_random_address(address)
        if adv_type == "Random"
        else None
    )

    now = current_time()

    if address not in devices:
        devices[address] = {
            "name": advertisement_data.local_name or device.name,
            "rssi": advertisement_data.rssi,
            "first_seen": now,
            "last_seen": now,
            "detections": 1,
            "address_type": adv_type,
            "random_address_type": random_type,
            "service_uuids": []
        }

    else:
        devices[address]["name"] = (
            advertisement_data.local_name
            or device.name
            or devices[address]["name"]
        )

        devices[address]["rssi"] = advertisement_data.rssi
        devices[address]["last_seen"] = now
        devices[address]["detections"] += 1
        devices[address]["address_type"] = adv_type
        devices[address]["random_address_type"] = random_type

    for uuid in service_uuids:
        if uuid not in devices[address]["service_uuids"]:
            devices[address]["service_uuids"].append(uuid)


def load_history():
    if not HISTORY_FILE.exists():
        return {}

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Aviso: arquivo de histórico inválido.")
        return {}


def save_history(history):
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


async def main():
    scanner = BleakScanner(detection_callback=callback)
    mac_lookup = AsyncMacLookup()

    print("Procurando dispositivos próximos...\n")

    await scanner.start()
    await asyncio.sleep(10)
    await scanner.stop()

    history = load_history()

    sorted_devices = sorted(
        devices.items(),
        key=lambda item: (
            item[1]["rssi"]
            if item[1]["rssi"] is not None
            else -100
        ),
        reverse=True
    )

    for address, info in sorted_devices:

        try:
            fabricante = await mac_lookup.lookup(address)
        except Exception:
            fabricante = "Não identificado"

        sinal = classify_signal(info["rssi"])

        identified_services = identify_services(
            info["service_uuids"]
        )

        previous = history.get(address, {})

        previous_uuids = previous.get("service_uuids", [])

        all_uuids = list(previous_uuids)

        for uuid in info["service_uuids"]:
            if uuid not in all_uuids:
                all_uuids.append(uuid)

        history[address] = {
            "name": info["name"] or previous.get("name"),

            "manufacturer": (
                fabricante
                if fabricante != "Não identificado"
                else previous.get("manufacturer", fabricante)
            ),

            "address_type": info["address_type"],

            "random_address_type": (
                info["random_address_type"]
                or previous.get("random_address_type")
            ),

            "service_uuids": all_uuids,

            "first_seen": previous.get(
                "first_seen",
                info["first_seen"]
            ),

            "last_seen": info["last_seen"],
            "last_rssi": info["rssi"],

            "total_detections": (
                previous.get("total_detections", 0)
                + info["detections"]
            )
        }

        print(f"Nome: {info['name']}")
        print(f"Endereço: {address}")
        print(f"Tipo de endereço: {info['address_type']}")

        if info["random_address_type"]:
            print(
                f"Subtipo de endereço: "
                f"{info['random_address_type']}"
            )

        print(f"Fabricante: {fabricante}")
        print(f"RSSI: {info['rssi']} dBm")
        print(f"Qualidade do sinal: {sinal}")
        print(f"Anúncios nesta varredura: {info['detections']}")

        if identified_services:
            print("UUIDs anunciados:")

            for service in identified_services:
                print(f"  UUID: {service['uuid']}")
                print(f"  Identificação: {service['name']}")

        else:
            print("UUIDs anunciados: Nenhum identificado")

        print("-" * 40)

    save_history(history)

    print(f"\nDispositivos encontrados nesta varredura: {len(devices)}")
    print(f"Dispositivos registrados no histórico: {len(history)}")
    print(f"Histórico salvo em: {HISTORY_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
