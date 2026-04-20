# ot_final.py
# Purpose: Passive OT Network Traffic Scanner for Green Energy Solutions
# This script monitors SCADA/ICS network traffic for OT-specific protocols
# (Modbus, DNP3, BACnet) without sending any packets or disrupting operations.
# All detected traffic is logged to ot_scan_log.txt for review.

import pyshark
import datetime

# Network interface to listen on - change this to match your environment
INTERFACE = "eth0"
LOG_FILE = "ot_scan_log.txt"


def log_data(data):
    """
    Logs OT traffic data securely to a file with a timestamp.
    Writes each entry to ot_scan_log.txt.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {data}\n"

    # Print to console for real-time visibility
    print(log_entry.strip())

    # Write log entry to file
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
    Initiates packet capture on the configured network interface.
    """
    log_data("OT Passive Scan Started")
    capture_packets(INTERFACE)
    log_data("OT Passive Scan Completed")


# README-style entry point message
if __name__ == "__main__":
    print("Passive Scanning Script for OT Environment")
    print("Ensure you have the correct network interface configured.")
    print("Logs will be stored in ot_scan_log.txt")
    main()
