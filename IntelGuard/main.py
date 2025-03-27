import subprocess
import json
import uuid

class PacketCapture:
    def __init__(self):
        self.interfaces = self.get_interfaces()
        self.object_id = str(uuid.uuid4())
        self.packet_tool = self.detect_packet_tool()

    def detect_packet_tool(self):
        """Detect whether nftables or iptables is available."""
        try:
            subprocess.run(["nft", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return "nftables"
        except FileNotFoundError:
            try:
                subprocess.run(["iptables", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return "iptables"
            except FileNotFoundError:
                raise EnvironmentError("Neither nftables nor iptables is available on this system.")

    def get_interfaces(self):
        """Retrieve available network interfaces."""
        result = subprocess.run(["ip", "link"], stdout=subprocess.PIPE, text=True)
        interfaces = []
        for line in result.stdout.splitlines():
            if ": " in line:
                interface = line.split(": ")[1].split("@")[0]
                if interface != "lo":  # Exclude loopback interface
                    interfaces.append(interface)
        return interfaces

    def display_interfaces(self):
        print("Available interfaces: ")
        for interface in self.interfaces:
            print(interface)

    def capture_packets(self, interface: str, **kwargs):
        if self.packet_tool == "nftables":
            print("Capturing packets using nftables...")
            command = f"sudo nft monitor trace > nftables_packets.log"
        elif self.packet_tool == "iptables":
            print("Capturing packets using iptables...")
            command = f"sudo iptables -A INPUT -i {interface} -j LOG --log-prefix 'IPTABLES_LOG: '"
        else:
            raise ValueError("Unsupported packet capturing tool.")

        print(f"Running command: {command}")
        subprocess.run(command, shell=True)
        print("Packet capture completed. Please check the logs.")

    def save_packets_to_json(self, packets):
        filename = f"packets_{self.object_id}.json"
        # Modify this method to handle the new packet data format
        # ...existing code...

def main():
    packet_capture = PacketCapture()
    print(f"Detected packet tool: {packet_capture.packet_tool}")
    packet_capture.display_interfaces()
    interface = input("Enter the interface to capture packets: ")
    packet_capture.capture_packets(interface)
    # Save packets logic may need to be updated based on the new capture method
    # ...existing code...

if __name__ == "__main__":
    main()
