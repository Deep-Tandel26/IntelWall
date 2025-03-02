import pyshark
import json

def test():
    capture = pyshark.LiveCapture(interface="wi-fi")
    packet_count = 0
    for packet in capture.sniff_continuously():
        data = f"source: {packet.ip.src}, destination: {packet.ip.dst}"
        if packet_count >= 10:
            break
        with open('data.json', 'w') as f:
            json.dump(data, f)
        packet_count += 1

test()

