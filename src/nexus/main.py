
import asyncio
from bleak import BleakScanner
from mac_vendor_lookup import AsyncMacLookup


devices = {}


def callback(device, advertisement_data):
    devices[device.address] = {
        "name": advertisement_data.local_name or device.name,
        "rssi": advertisement_data.rssi
    }


async def main():
    scanner = BleakScanner(detection_callback=callback)
    mac_lookup = AsyncMacLookup()

    print("Procurando dispositivos próximos...\n")

    await scanner.start()
    await asyncio.sleep(10)
    await scanner.stop()

    for address, info in devices.items():

        try:
           fabricante = await mac_lookup.lookup(address)
        except Exception as erro:
            fabricante = f"Erro na consulta: {erro}"

        print(f"Nome: {info['name']}")
        print(f"Endereço: {address}")
        print(f"Fabricante: {fabricante}")
        print(f"RSSI: {info['rssi']} dBm")
        print("-" * 40)


asyncio.run(main())
