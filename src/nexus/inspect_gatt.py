"""Interactive, read-only GATT service and characteristic inspection."""

import asyncio

from bleak import BleakClient, BleakScanner


SCAN_SECONDS = 10


def choose_device(devices_and_advertisements):
    for index, (device, advertisement) in enumerate(
        devices_and_advertisements, start=1
    ):
        name = advertisement.local_name or device.name or "Nome não anunciado"
        rssi = advertisement.rssi
        signal = f"{rssi} dBm" if rssi is not None else "RSSI indisponível"
        print(f"{index}. {name} | {device.address} | {signal}")

    while True:
        answer = input("\nNúmero do dispositivo (Enter para sair): ").strip()
        if not answer:
            return None
        if (
            answer.isdecimal()
            and 1 <= int(answer) <= len(devices_and_advertisements)
        ):
            return devices_and_advertisements[int(answer) - 1][0]
        print("Seleção inválida.")


def print_gatt_tree(services):
    if not services:
        print("Nenhum serviço GATT foi exposto pelo dispositivo.")
        return

    for service in services:
        print(f"\nServiço: {service.uuid}")
        if service.description:
            print(f"  Descrição: {service.description}")

        if not service.characteristics:
            print("  Nenhuma característica")
            continue

        for characteristic in service.characteristics:
            print(f"  Característica: {characteristic.uuid}")
            if characteristic.description:
                print(f"    Descrição: {characteristic.description}")
            properties = ", ".join(characteristic.properties) or "nenhuma"
            print(f"    Propriedades: {properties}")


async def main():
    print(f"Procurando dispositivos BLE por {SCAN_SECONDS} segundos...\n")
    discovered = await BleakScanner.discover(
        timeout=SCAN_SECONDS,
        return_adv=True,
    )
    devices_and_advertisements = sorted(
        discovered.values(),
        key=lambda item: item[1].rssi if item[1].rssi is not None else -100,
        reverse=True,
    )

    if not devices_and_advertisements:
        print("Nenhum dispositivo BLE encontrado.")
        return

    device = choose_device(devices_and_advertisements)
    if device is None:
        print("Inspeção cancelada.")
        return

    print(
        f"\nConectando a {device.name or device.address} para enumerar "
        "serviços e características GATT. Nenhum valor será lido ou gravado."
    )

    try:
        async with BleakClient(device, timeout=20) as client:
            print_gatt_tree(client.services)
    except Exception as exc:
        print(f"Não foi possível inspecionar o dispositivo: {exc}")

    print("\nInspeção encerrada.")


if __name__ == "__main__":
    asyncio.run(main())
