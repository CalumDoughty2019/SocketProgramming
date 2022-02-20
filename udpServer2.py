import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

def create_socket():
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    return server_socket

def handle_recd_datagram(recd_datagram):
    message = recd_datagram[0]
    address = recd_datagram[1]
    client_ip_address = address[0]
    client_port = address[1]
    print("Received message of length ", len(message), "bytes)")

    client_msg = "Message from client:{}".format(message)
    client_ip = "Client IP Address:{}".format(client_ip_address)
    client_ip_port = "CLient IP Port:{}".format(client_port)

    print(client_msg)
    print(client_ip)
    print(client_ip_port)
    return address, message

def main():
    udp_server_socket = create_socket()
    udp_server_socket.bind((localIP, localPort))
    print("UDP server up and listening")
    while True:
        new_datagram = udp_server_socket.recvfrom(bufferSize)
        address, message = handle_recd_datagram(new_datagram)

        # Sending reply to client
        if len(message) < 10:
            msg_to_send = "Hello UDP Client, you are not very talkative today?"
        else:
            msg_to_send = "Hello UDP Client, always good to chat with you, how can I help you today?"

        bytes_to_send = str.encode(msg_to_send)
        udp_server_socket.sendto(bytes_to_send, address)

main()