# NEXUS IoT

### Wireless & IoT Security Toolkit

**NEXUS** is an open-source Python project focused on wireless device discovery, IoT investigation, network monitoring, and security analysis.

The goal is to build a modular toolkit capable of identifying wireless devices, inspecting available services, monitoring connection behavior, detecting suspicious events, and supporting authorized device management.

The project combines practical experimentation, protocol analysis, and cybersecurity concepts in a single platform.

---

## Project Vision

NEXUS aims to become a unified environment for investigating and monitoring Wi-Fi and Bluetooth devices.

Its long-term objectives include:

- Discovering nearby wireless devices and networks.
- Identifying device manufacturers and technical information.
- Inspecting Bluetooth services and characteristics.
- Monitoring device availability and connection events.
- Detecting unusual wireless activity and network anomalies.
- Supporting authorized device management.
- Generating security reports and investigation logs.

## Current Features

The following components are currently implemented:

| Module | Description | Status |
|---|---|---|
| BLE Scanner | Discovers nearby Bluetooth Low Energy devices. | Implemented |
| GATT Inspector | Inspects available GATT services and characteristics. | Implemented |
| Signal Simulator | Simulates RSSI attenuation, noise, and detection loss. | Implemented |
| Disconnect Monitor Simulator | Simulates correlated device disconnection events. | Implemented |
| JSON History | Stores device discovery history. | Implemented |

## Development Roadmap

### 1. Wireless Discovery
- Wi-Fi network discovery.
- Wireless access point identification.
- Device discovery and classification.
- Bluetooth Classic investigation.

### 2. Device Intelligence
- Manufacturer identification.
- Protocol and service inspection.
- Device information collection.
- Historical device tracking.

### 3. Network Monitoring
- Device availability monitoring.
- Connection event tracking.
- Signal strength analysis.
- Anomaly detection.

### 4. Security Analysis
- Suspicious device detection.
- Access point identification.
- Wireless security configuration analysis.
- Detection of unusual connection patterns.

### 5. Device Management
- Authorized device disconnection.
- Network access management through supported administrative interfaces.
- Device status monitoring.
- Connection management.

### 6. Reporting & Visualization
- Interactive dashboard.
- Network topology visualization.
- Security alerts.
- Investigation history.
- Automated security reports.

## Technologies

- Python 3.14
- Bleak
- Bluetooth Low Energy (BLE)
- GATT
- Wi-Fi networking
- JSON
- Git

Additional libraries and tools will be introduced as development progresses.

## Project Structure

```text
nexus-iot/
│
├── src/
│   └── nexus/
│       ├── main.py
│       ├── inspect_gatt.py
│       ├── simulate_signal.py
│       └── simulate_disconnect_monitor.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/rafaelalsilveira/nexus-iot.git
```

Navigate to the project directory:

```bash
cd nexus-iot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### BLE Device Scanner

```bash
python src/nexus/main.py
```

Discovers nearby Bluetooth Low Energy devices and collects available information.

### GATT Inspector

```bash
python src/nexus/inspect_gatt.py
```

Connects to a selected BLE device and inspects its available GATT services and characteristics in read-only mode.

### Signal Simulation

```bash
python src/nexus/simulate_signal.py --base-rssi -55 --attenuation 20 --noise 4 --loss 15 --samples 20 --seed 7
```

Simulates wireless signal attenuation, noise, and detection loss without transmitting radio signals.

### Disconnect Monitoring Simulation

```bash
python src/nexus/simulate_disconnect_monitor.py --devices 8 --background-drops 3 --bursts 2 --threshold 3 --window 2 --seed 7
```

Simulates device disconnection events and identifies correlated occurrences.

## Security & Responsible Use

NEXUS is designed for educational purposes, cybersecurity research, and authorized testing in controlled environments.

The project focuses on wireless analysis, device monitoring, security assessment, and legitimate device management.

All testing should be performed on devices and networks owned by the user or with explicit authorization.

## Project Status

**Under active development.**

NEXUS is evolving from an initial BLE discovery tool into a broader wireless and IoT security toolkit.

New modules and capabilities will be introduced progressively.

## Author

**Rafaela Silveira**

GitHub: [@rafaelalsilveira](https://github.com/rafaelalsilveira)

---

*Explore. Analyze. Understand. Secure.*

