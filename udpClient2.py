import socket
import sys

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

def create_socket():
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    return client_socket

def msg_to_send():
    new_msg = input("Please enter the message you wish to send or Q to quit > ")
    if new_msg == "Q":
        print("BYE...")
        sys.exit(0)
    bytes_to_send = str.encode(new_msg)
    return bytes_to_send

def main():
    while True:
        stuff_to_send = msg_to_send()
        udp_client_socket = create_socket()
        udp_client_socket.sendto(stuff_to_send, serverAddressPort)
        msg_from_server = udp_client_socket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msg_from_server[0])
        print(msg)

main()