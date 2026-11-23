# NEXUS IoT

### Wireless & Network Security Platform

[English](#english) | [Português](#português)

---

<a name="english"></a>

# 🇺🇸 English

## About the Project

**NEXUS** is a Python-based security platform under development, focused on wireless networks, connected devices and IoT infrastructure monitoring.

Initially designed for **Small and Medium-sized Businesses (SMBs)**, NEXUS aims to provide network visibility, device discovery, anomaly detection, security assessment and authorized incident response.

The project combines Python development, network protocols, wireless technologies and practical security investigation.

> **Project status:** Under active development. Some capabilities described in this document are planned and have not yet been implemented.

## Project Vision

Small and medium-sized businesses often lack visibility into the devices connected to their networks.

Unknown devices, exposed services, unexpected connectivity changes and poorly monitored IoT equipment can introduce security risks.

NEXUS aims to address these challenges through a centralized platform capable of discovering devices, maintaining an asset inventory, monitoring network changes and supporting security investigations.

## Core Modules

### 1. NEXUS Discovery
*Network Asset Discovery & Inventory*

Planned capabilities:
- Discover devices on local networks.
- Identify IP and MAC addresses.
- Identify manufacturers when information is available.
- Maintain a persistent device inventory.
- Integrate Wi-Fi, Ethernet and Bluetooth discovery.

**Business value:** Provide visibility into the devices connected to a company's infrastructure.

### 2. NEXUS Sentinel
*Network Monitoring & Anomaly Detection*

Planned capabilities:
- Periodic network monitoring.
- Detection of newly discovered devices.
- Identification of devices that become unavailable.
- Comparison against known device inventories.
- Event generation and security alerts.

**Business value:** Identify unknown devices and unexpected network changes.

### 3. NEXUS Inspector
*Network Security Assessment*

Planned capabilities:
- Service and port discovery.
- Protocol investigation.
- Identification of potentially exposed services.
- Security configuration assessment.
- Evidence-based risk identification.

**Business value:** Identify potential network exposure and security weaknesses.

### 4. NEXUS Response
*Authorized Device Management*

Planned capabilities:
- Router administration integrations.
- Authorized device access management.
- Administrative blocking requests where supported.
- Verification of administrative actions.
- Auditable response records.

**Business value:** Support incident response through authorized administrative controls.

NEXUS will not rely on wireless deauthentication attacks or radio interference to disconnect devices.

### 5. NEXUS Intelligence
*Security Events & Reporting*

Planned capabilities:
- Structured event logging.
- Security event correlation.
- Device risk classification.
- Historical records.
- Technical and executive reports.

**Business value:** Transform technical information into actionable security insights.

### 6. NEXUS Console
*Security Management Dashboard*

Planned capabilities:
- Centralized device inventory.
- Network monitoring dashboard.
- Security alerts.
- Investigation interface.
- User and permission management.

**Business value:** Provide a centralized and accessible security management experience.

---

## Current Implementations

The following capabilities are already present in the codebase.

### Bluetooth Low Energy (BLE)

- BLE device discovery using Bleak.
- Device name and address identification.
- RSSI signal strength classification.
- Manufacturer identification when available.
- Advertisement UUID collection.
- First and last detection tracking.
- Detection counter.
- Persistent JSON device history.

### GATT Inspection

- Inspection of BLE services.
- Characteristic enumeration.
- GATT structure investigation.

### Offline Simulations

- Signal attenuation and detection loss simulation.
- Simulated device disconnection monitoring.
- Artificial event generation for controlled experiments.

Simulators operate offline and do not interfere with real wireless devices.

---

## Real-World Testing Laboratory

NEXUS will be developed and validated using real equipment in a controlled home network environment.

### Initial Laboratory Equipment

| Equipment | Testing Objectives |
|---|---|
| IP Security Camera | Network discovery and service investigation |
| Network Printer | Device identification and exposed services |
| Windows PC | Network visibility and service assessment |
| Second PC | Multi-device monitoring |
| Smartphones | Wireless discovery and connectivity changes |
| Tablet | Device discovery and network monitoring |

The laboratory will support practical experiments, repeatable tests, evidence collection and technical documentation.

The objective is to validate NEXUS against real devices rather than relying exclusively on simulated scenarios.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Bleak | Bluetooth Low Energy |
| Scapy | Planned network discovery and analysis |
| SQLite | Planned structured persistence |
| FastAPI | Planned backend API |
| Pytest | Automated testing |
| GitHub Actions | Planned CI/CD |
| Streamlit / Web UI | Planned dashboard |

Technologies listed as planned are not necessarily implemented.

---

## Development Roadmap

- [x] Initial BLE scanner.
- [x] BLE manufacturer identification.
- [x] RSSI classification.
- [x] Persistent JSON device history.
- [x] GATT inspection.
- [x] Offline signal simulation.
- [x] Offline disconnection simulation.
- [ ] Automated tests with Pytest.
- [ ] Network device discovery.
- [ ] Persistent network asset inventory.
- [ ] Network monitoring and anomaly detection.
- [ ] Structured security event logging.
- [ ] Service and port assessment.
- [ ] Security reporting.
- [ ] Authorized router administration integrations.
- [ ] Centralized security dashboard.
- [ ] Multi-network management architecture.

---

## Architecture Goals

NEXUS is being designed around a modular architecture with independent components for:

- Device discovery.
- Asset inventory.
- Monitoring and detection.
- Security assessment.
- Incident response.
- Event processing and reporting.
- User interface.

The initial deployment target is local installation within the monitored network, with an architecture that can evolve toward centralized multi-network management.

---

## Security Principles

- Authorized environments only.
- No wireless deauthentication attacks.
- No unauthorized device disconnection.
- Administrative actions must use supported management interfaces.
- Security findings should include supporting evidence.
- Monitoring and simulation must remain clearly distinguished.
- Actions must be auditable.

---

## Repository Structure

```text
nexus-iot/
├── data/
├── docs/
├── src/
│   └── nexus/
│       ├── __init__.py
│       ├── main.py
│       ├── inspect_gatt.py
│       ├── simulate_disconnect_monitor.py
│       └── simulate_signal.py
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Project Objective

NEXUS is an ongoing cybersecurity engineering project focused on practical network security, wireless technologies and IoT infrastructure monitoring.

The goal is to develop a functional, testable and extensible platform capable of solving real network visibility and security monitoring problems for small and medium-sized businesses.

**Built with Python. Developed through real-world experimentation. Focused on practical security.**

---

<a name="português"></a>

# 🇧🇷 Português

## Sobre o Projeto

**NEXUS** é uma plataforma de segurança desenvolvida em Python, voltada para redes sem fio, dispositivos conectados e monitoramento de infraestrutura IoT.

Inicialmente direcionado a **pequenas e médias empresas (PMEs)**, o NEXUS tem como objetivo oferecer visibilidade da rede, descoberta de dispositivos, detecção de anomalias, avaliação de segurança e suporte à resposta autorizada a incidentes.

O projeto combina desenvolvimento Python, protocolos de rede, tecnologias wireless e investigação prática em cibersegurança.

> **Status do projeto:** Em desenvolvimento ativo. Algumas funcionalidades descritas neste documento estão planejadas e ainda não foram implementadas.

## Visão do Projeto

Pequenas e médias empresas frequentemente não possuem visibilidade suficiente sobre os dispositivos conectados às suas redes.

Dispositivos desconhecidos, serviços expostos, alterações inesperadas de conectividade e equipamentos IoT sem monitoramento adequado podem representar riscos de segurança.

O NEXUS busca solucionar esses problemas por meio de uma plataforma centralizada capaz de descobrir dispositivos, manter um inventário de ativos, monitorar alterações na rede e apoiar investigações de segurança.

## Módulos Principais

### 1. NEXUS Discovery
*Descoberta e Inventário de Ativos de Rede*

Funcionalidades planejadas:
- Descoberta de dispositivos na rede local.
- Identificação de endereços IP e MAC.
- Identificação de fabricantes quando disponível.
- Manutenção de inventário persistente de dispositivos.
- Integração com descoberta Wi-Fi, Ethernet e Bluetooth.

**Valor comercial:** oferecer visibilidade sobre os equipamentos conectados à infraestrutura da empresa.

### 2. NEXUS Sentinel
*Monitoramento de Rede e Detecção de Anomalias*

Funcionalidades planejadas:
- Monitoramento periódico da rede.
- Detecção de novos dispositivos.
- Identificação de dispositivos que ficam indisponíveis.
- Comparação com inventários de dispositivos conhecidos.
- Geração de eventos e alertas de segurança.

**Valor comercial:** identificar dispositivos desconhecidos e alterações inesperadas na rede.

### 3. NEXUS Inspector
*Avaliação de Segurança da Rede*

Funcionalidades planejadas:
- Descoberta de serviços e portas.
- Investigação de protocolos.
- Identificação de serviços potencialmente expostos.
- Avaliação de configurações de segurança.
- Identificação de riscos baseada em evidências.

**Valor comercial:** identificar possíveis exposições e fragilidades na infraestrutura.

### 4. NEXUS Response
*Gerenciamento Autorizado de Dispositivos*

Funcionalidades planejadas:
- Integração com administração de roteadores.
- Gerenciamento autorizado de acesso de dispositivos.
- Solicitação de bloqueio administrativo quando houver suporte.
- Verificação das ações administrativas.
- Registro auditável das respostas.

**Valor comercial:** apoiar a resposta a incidentes utilizando controles administrativos autorizados.

O NEXUS não utilizará ataques de desautenticação wireless ou interferência de rádio para desconectar dispositivos.

### 5. NEXUS Intelligence
*Eventos de Segurança e Relatórios*

Funcionalidades planejadas:
- Registro estruturado de eventos.
- Correlação de eventos de segurança.
- Classificação de risco dos dispositivos.
- Histórico de ocorrências.
- Relatórios técnicos e executivos.

**Valor comercial:** transformar informações técnicas em indicadores úteis para decisões de segurança.

### 6. NEXUS Console
*Painel de Gerenciamento de Segurança*

Funcionalidades planejadas:
- Inventário centralizado de dispositivos.
- Dashboard de monitoramento.
- Alertas de segurança.
- Interface de investigação.
- Gerenciamento de usuários e permissões.

**Valor comercial:** oferecer uma experiência centralizada e acessível para gerenciamento da segurança.

---

## Funcionalidades Implementadas

As seguintes funcionalidades já estão presentes no código do projeto.

### Bluetooth Low Energy (BLE)

- Descoberta de dispositivos BLE utilizando Bleak.
- Identificação de nomes e endereços de dispositivos.
- Classificação da intensidade do sinal RSSI.
- Identificação de fabricantes quando disponível.
- Coleta de UUIDs anunciados.
- Registro da primeira e última detecção.
- Contagem de detecções.
- Histórico persistente de dispositivos em JSON.

### Inspeção GATT

- Inspeção de serviços BLE.
- Enumeração de características.
- Investigação da estrutura GATT.

### Simulações Offline

- Simulação de atenuação de sinal e perda de detecção.
- Simulação de monitoramento de desconexões.
- Geração artificial de eventos para experimentos controlados.

Os simuladores operam offline e não interferem em dispositivos wireless reais.

---

## Laboratório de Testes em Ambiente Real

O NEXUS será desenvolvido e validado utilizando equipamentos reais em um ambiente de rede doméstico controlado.

### Equipamentos Iniciais do Laboratório

| Equipamento | Objetivos dos testes |
|---|---|
| Câmera de segurança IP | Descoberta de rede e investigação de serviços |
| Impressora de rede | Identificação de dispositivos e serviços expostos |
| PC com Windows | Visibilidade de rede e avaliação de serviços |
| Segundo PC | Monitoramento de múltiplos dispositivos |
| Smartphones | Descoberta wireless e alterações de conectividade |
| Tablet | Descoberta de dispositivos e monitoramento de rede |

O laboratório permitirá realizar experimentos práticos, testes reproduzíveis, coleta de evidências e documentação técnica.

O objetivo é validar o NEXUS com dispositivos reais, em vez de depender exclusivamente de cenários simulados.

---

## Tecnologias

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento principal |
| Bleak | Bluetooth Low Energy |
| Scapy | Descoberta e análise de rede planejadas |
| SQLite | Persistência estruturada planejada |
| FastAPI | API backend planejada |
| Pytest | Testes automatizados |
| GitHub Actions | CI/CD planejado |
| Streamlit / Web UI | Dashboard planejado |

As tecnologias indicadas como planejadas ainda não necessariamente estão implementadas.

---

## Roadmap de Desenvolvimento

- [x] Scanner BLE inicial.
- [x] Identificação de fabricantes BLE.
- [x] Classificação RSSI.
- [x] Histórico persistente de dispositivos em JSON.
- [x] Inspeção GATT.
- [x] Simulação offline de sinal.
- [x] Simulação offline de desconexões.
- [ ] Testes automatizados com Pytest.
- [ ] Descoberta de dispositivos na rede.
- [ ] Inventário persistente de ativos de rede.
- [ ] Monitoramento de rede e detecção de anomalias.
- [ ] Registro estruturado de eventos de segurança.
- [ ] Avaliação de serviços e portas.
- [ ] Relatórios de segurança.
- [ ] Integrações autorizadas com administração de roteadores.
- [ ] Dashboard centralizado de segurança.
- [ ] Arquitetura para gerenciamento de múltiplas redes.

---

## Objetivos de Arquitetura

O NEXUS está sendo projetado com uma arquitetura modular, composta por componentes independentes para:

- Descoberta de dispositivos.
- Inventário de ativos.
- Monitoramento e detecção.
- Avaliação de segurança.
- Resposta a incidentes.
- Processamento de eventos e relatórios.
- Interface de usuário.

O objetivo inicial é permitir a instalação local na rede monitorada, mantendo uma arquitetura que possa evoluir futuramente para o gerenciamento centralizado de múltiplas redes.

---

## Princípios de Segurança

- Utilização somente em ambientes autorizados.
- Nenhum ataque de desautenticação wireless.
- Nenhuma desconexão não autorizada de dispositivos.
- Ações administrativas devem utilizar interfaces de gerenciamento suportadas.
- Descobertas de segurança devem apresentar evidências.
- Monitoramento e simulação devem permanecer claramente diferenciados.
- Todas as ações administrativas devem ser auditáveis.

---

## Objetivo do Projeto

O NEXUS é um projeto contínuo de engenharia em cibersegurança, com foco em segurança prática de redes, tecnologias wireless e monitoramento de infraestrutura IoT.

O objetivo é desenvolver uma plataforma funcional, testável e extensível, capaz de solucionar problemas reais de visibilidade e monitoramento de segurança em pequenas e médias empresas.

**Desenvolvido em Python. Validado com experimentos reais. Focado em segurança prática.**