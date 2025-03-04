import pyshark
from typing import Optional, Any
import json
import uuid

class PacketCapture:
    def __init__(self):
        self.interfaces = pyshark.tshark.tshark.get_all_tshark_interfaces_names()
        self.object_id = str(uuid.uuid4())

    def display_interfaces(self):
        print("Available interfaces: ")
        for interface in self.interfaces:
            print(interface)

    def capture_packets(
        self, 
        interface: str,  
        **kwargs
    ):
        capture = pyshark.LiveCapture(
            interface=interface, 
            **kwargs
        )
        result = capture.sniff_continuously(
            packet_count=10,
            **kwargs
        )
        return result

    def save_packets_to_json(self, packets):
        filename = f"packets_{self.object_id}.json"
        packet_list = []
        for packet in packets:
            packet_info = {
                "source_ip": packet.ip.src,
                "destination_ip": packet.ip.dst,
                "protocol": packet.transport_layer,
                "length": packet.length
            }
            packet_list.append(packet_info)
        with open(filename, 'w') as f:
            json.dump(packet_list, f, indent=4)
        print(f"Packets saved to {filename}")

def main():
    packet_capture = PacketCapture()
    packet_capture.display_interfaces()
    interface = input("Enter the interface to capture packets: ")
    packets = packet_capture.capture_packets(interface)
    packet_capture.save_packets_to_json(packets)

if __name__ == "__main__":
    main()
