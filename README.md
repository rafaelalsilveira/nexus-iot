
# NEXUS IoT

Scanner de dispositivos Bluetooth Low Energy (BLE) desenvolvido em Python.

## Funcionalidades

- Descoberta de dispositivos BLE próximos.
- Identificação de nome e endereço MAC.
- Leitura da intensidade do sinal (RSSI).
- Consulta do fabricante pelo endereço MAC.
- Inspeção interativa e somente leitura de serviços e características GATT.

## Tecnologias

- Python 3.14
- Bleak
- MAC Vendor Lookup

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o scanner:

```bash
python src/nexus/main.py
```

Para escolher um dispositivo BLE encontrado e inspecionar os serviços e as
propriedades das características GATT:

```bash
python src/nexus/inspect_gatt.py
```

O inspetor conecta-se ao dispositivo selecionado para enumerar a árvore GATT.
Ele não lê nem grava valores de características e encerra a conexão ao terminar.

Para demonstrar atenuação, ruído e perda de detecções sem transmitir no rádio:

```bash
python src/nexus/simulate_signal.py --base-rssi -55 --attenuation 20 --noise 4 --loss 15 --samples 20 --seed 7
```

O simulador usa apenas números artificiais e não interage com dispositivos Bluetooth.

Para demonstrar detecção de quedas correlacionadas com eventos artificiais:

```bash
python src/nexus/simulate_disconnect_monitor.py --devices 8 --background-drops 3 --bursts 2 --threshold 3 --window 2 --seed 7
```

Esse monitor é uma simulação offline: não envia comandos, desconecta clientes nem captura tráfego.

## Status

🚧 Projeto em desenvolvimento.
