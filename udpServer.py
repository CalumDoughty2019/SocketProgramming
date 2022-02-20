import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Hello UDP Client, thanks for reaching out to me, what can I do for you today?"
bytesToSend = str.encode(msgFromServer) # turn this text message into a bytestream for socket programming

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

# Listen for incoming datagrams
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    messageLength = len(message)
    print("Received message of length", messageLength, "bytes)")

    address = bytesAddressPair[1]
    clientIPAddress = address[0]
    clientPort = address[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(clientIPAddress)
    clientIPPort = "Client IP Port:{}".format(clientPort)

    print(clientMsg)
    print(clientIP)
    print(clientIPPort)

    # Sending reply to client
    UDPServerSocket.sendto(bytesToSend, address)