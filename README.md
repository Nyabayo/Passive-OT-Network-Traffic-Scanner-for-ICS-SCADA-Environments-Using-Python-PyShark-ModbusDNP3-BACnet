# 🔐 Passive-OT-Network-Traffic-Scanner-for-ICS-SCADA-Environments-Using-Python-PyShark-Modbus-DNP3-BACnet

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![PyShark](https://img.shields.io/badge/PyShark-Packet%20Capture-green?style=for-the-badge)
![OT Security](https://img.shields.io/badge/OT%20Security-ICS%2FSCADA-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

---

## 📖 Overview

This project is a **passive Operational Technology (OT) network traffic scanner** built in Python for monitoring Industrial Control System (ICS) and Supervisory Control and Data Acquisition (SCADA) environments. It is designed to identify devices communicating over OT-specific protocols such as **Modbus**, **DNP3**, and **BACnet** — without sending a single packet or interfering with live industrial operations.

> ⚠️ **This tool is strictly passive. It does not transmit packets, execute exploits, or disrupt any industrial process.**

Developed as part of a cybersecurity training lab simulating a real-world analyst role at **Green Energy Solutions**, a fictional ICS operator managing power plant infrastructure.

---

## 🏭 Background: What is OT Security?

**Operational Technology (OT)** refers to hardware and software systems that monitor and control physical processes in critical infrastructure sectors including:

| Sector | Example OT Use Case |
|---|---|
| ⚡ Energy | SCADA monitoring electrical substations and grid loads |
| 🚰 Water Treatment | Flow control, chemical dosing, contamination detection |
| 🚆 Transportation | Train signaling, air traffic control, traffic synchronization |
| 🏭 Manufacturing | PLCs controlling assembly lines and quality control |
| 🏥 Healthcare | Building management and medical device control |

Unlike **IT security** which prioritizes **Confidentiality, Integrity, and Availability (CIA)**, OT security prioritizes:

- ✅ **Safety** — protecting human life and the environment
- ✅ **Availability** — systems must run continuously without interruption
- ✅ **Reliability** — consistent and predictable operation at all times

---

## 🧩 Key OT Components

```
OT Environment
├── SCADA  (Supervisory Control and Data Acquisition)
│   └── Centralized monitoring and control of geographically dispersed operations
├── ICS    (Industrial Control Systems)
│   └── Integrated hardware/software managing industrial automation
├── PLC    (Programmable Logic Controller)
│   └── Rugged digital computers controlling machinery on factory floors
├── RTU    (Remote Terminal Unit)
│   └── Field devices collecting sensor data and executing control commands
├── HMI    (Human-Machine Interface)
│   └── Visual dashboard for operators to monitor and adjust systems
└── DCS    (Distributed Control System)
    └── Controls complex, geographically distributed industrial processes
```

---

## 🌐 OT Protocols Monitored

| Protocol | Full Name | Port | Used In |
|---|---|---|---|
| **Modbus** | Modbus TCP/RTU | 502 | PLCs, RTUs, manufacturing |
| **DNP3** | Distributed Network Protocol 3 | 20000 | Utilities, water, energy |
| **BACnet** | Building Automation and Control Networks | 47808 | HVAC, building management |

> These protocols were designed for reliability, **not security**. They lack encryption and authentication, making passive monitoring essential for threat detection.

---

## ⚙️ Features

- 🔍 **Passive packet capture** using PyShark — zero packets transmitted
- 📡 **OT protocol detection** for Modbus, DNP3, and BACnet traffic
- 🖥️ **Metadata extraction** including source IP, destination IP, and protocol layer
- 📝 **Secure timestamped logging** to `ot_scan_log.txt`
- 🛡️ **Robust error handling** to prevent crashes in sensitive environments
- 💬 **Operator-friendly console output** with README-style startup messages

---

## 🗂️ Project Structure

```
Passive-OT-Network-Traffic-Scanner/
│
├── ot_final.py          # Main passive scanning script
└── README.md            # Project documentation
```

---

## 🐍 The Python Script

```python
# ot_final.py
# Purpose: Passive OT Network Traffic Scanner for Green Energy Solutions
# This script monitors SCADA/ICS network traffic for OT-specific protocols
# (Modbus, DNP3, BACnet) without sending any packets or disrupting operations.
# All detected traffic is logged to ot_scan_log.txt for review.

import pyshark
import datetime

INTERFACE = "eth0"
LOG_FILE = "ot_scan_log.txt"


def log_data(data):
    """
    Logs OT traffic data securely to a file with a timestamp.
    Writes each entry to ot_scan_log.txt.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {data}\n"
    print(log_entry.strip())
    with open("ot_scan_log.txt", "a") as log_file:
        log_file.write(log_entry)


def filter_ot_traffic(packet):
    """
    Filters packets to identify OT-related traffic.
    Checks for Modbus, DNP3, and BACnet protocols and extracts metadata.
    """
    try:
        if 'MODBUS' in packet or 'DNP3' in packet or 'BACnet' in packet:
            src_ip = packet.ip.src
            dest_ip = packet.ip.dst
            protocol = packet.highest_layer
            log_data(f"OT Traffic Detected: {protocol} from {src_ip} to {dest_ip}")
    except AttributeError:
        pass  # Ignore packets without IP or protocol layers


def capture_packets(interface):
    """
    Capture packets passively and handle errors.
    Listens on the specified network interface without sending any packets.
    """
    try:
        print(f"Listening on {interface}...")
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously(packet_count=50):
            try:
                filter_ot_traffic(packet)
            except Exception as e:
                print(f"Error processing packet: {e}")
    except Exception as e:
        print(f"Error capturing packets: {e}")


def main():
    """
    Main function to start the passive OT network scanner.
    """
    log_data("OT Passive Scan Started")
    capture_packets(INTERFACE)
    log_data("OT Passive Scan Completed")


if __name__ == "__main__":
    print("Passive Scanning Script for OT Environment")
    print("Ensure you have the correct network interface configured.")
    print("Logs will be stored in ot_scan_log.txt")
    main()
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- TShark (Wireshark CLI) installed on your system
- PyShark library

### Installation

```bash
# Clone the repository
git clone https://github.com/Nyabayo/Passive-OT-Network-Traffic-Scanner-for-ICS-SCADA-Environments-Using-Python-PyShark-ModbusDNP3-BACnet.git

# Navigate into the directory
cd Passive-OT-Network-Traffic-Scanner-for-ICS-SCADA-Environments-Using-Python-PyShark-ModbusDNP3-BACnet.git

# Install dependencies
pip install pyshark
```

### Configuration

Open `ot_final.py` and update the network interface to match your environment:

```python
# Windows example
INTERFACE = "Wi-Fi"

# macOS example
INTERFACE = "en0"

# Linux example
INTERFACE = "eth0"
```

### Running the Script

```bash
# Run with admin/root privileges (required for packet capture)
sudo python3 ot_final.py
```

### Sample Output

```
Passive Scanning Script for OT Environment
Ensure you have the correct network interface configured.
Logs will be stored in ot_scan_log.txt
[2026-04-20 14:32:01] OT Passive Scan Started
Listening on eth0...
[2026-04-20 14:32:05] OT Traffic Detected: MODBUS from 192.168.1.10 to 192.168.1.50
[2026-04-20 14:32:09] OT Traffic Detected: DNP3 from 192.168.1.20 to 192.168.1.50
[2026-04-20 14:32:15] OT Traffic Detected: BACnet from 192.168.1.30 to 192.168.1.50
[2026-04-20 14:33:01] OT Passive Scan Completed
```

---

## 🛡️ Common OT Vulnerabilities Addressed

| Vulnerability | Description | Mitigation |
|---|---|---|
| 🔓 Insecure Protocols | Modbus/DNP3 lack encryption | Monitor traffic, use VPNs and secure tunnels |
| 🕰️ Legacy Systems | Outdated unpatched software | Compensating controls, allowlisting, segmentation |
| 🌐 Flat Networks | No segmentation between OT/IT | Implement VLANs, firewalls, DMZs |
| 👤 Weak Authentication | Default or no credentials | MFA, RBAC, strong password policies |
| 📉 Insufficient Monitoring | No visibility into OT traffic | Deploy OT-specific IDS/IPS and SIEM |
| 🏢 Physical Security | Unauthorized physical access | Access controls, biometrics, surveillance |
| 🕵️ Insider Threats | Negligent or malicious insiders | User behavior analytics, activity monitoring |

---

## 📋 OT vs IT Penetration Testing

| Aspect | IT Penetration Testing | OT Penetration Testing |
|---|---|---|
| **Primary Goal** | Find data vulnerabilities | Ensure operational safety |
| **Techniques** | Aggressive scanning, exploitation | Passive reconnaissance, non-intrusive |
| **Tools** | Nmap, Metasploit, Burp Suite | Wireshark, Nessus Industrial, custom scripts |
| **Risk Level** | Data loss, downtime | Physical harm, equipment damage |
| **Coordination** | IT security teams | Operational teams, engineers, management |
| **Regulations** | GDPR, HIPAA | NERC CIP, ISA/IEC 62443 |

---

## 📜 Compliance and Standards

- 🏛️ **NERC CIP** — North American Electric Reliability Corporation Critical Infrastructure Protection
- 🔧 **ISA/IEC 62443** — Industrial Automation and Control Systems Security
- 🌍 **NIST SP 800-82** — Guide to Industrial Control Systems Security

---

## ⚠️ Disclaimer

> This tool is intended for **authorized security monitoring and educational purposes only**. Always obtain proper written authorization before scanning any network. Unauthorized use against systems you do not own or have permission to test is illegal and unethical. The author accepts no liability for misuse.

---

## 👨‍💻 Author

**Ernest Osindo**
Cybersecurity Analyst in Training
📍 Kenya

---

## 🙏 Acknowledgements

Special thanks to **Brian Wafula** (Technical Mentor) for the guidance and support throughout this module. 🙌

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

⭐ **If you found this project useful, please give it a star!** ⭐
