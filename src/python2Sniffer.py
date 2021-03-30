import socket
import struct
import binascii

# use socket.PF_PACKET for linux, or socket.AF_INET for windows
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket. htons(0x0800))
while True:
    # to receive the packet
    packet = s.recvfrom(2048)
    # rip the ethernet header
    ethernet_header = packet[0][0:14]
    # parse and unpack the header with the struct method
    eth_header = struct.unpack("!6s6s2s", ethernet_header)
    # return the hex values 
    print("Destination MAC:" + binascii.hexlify(eth_header[0]) + " Source MAC:"
        + binascii.hexlify(eth_header[1]) + " Type:"
        + binascii.hexlify(eth_header[2]))
