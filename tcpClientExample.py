import socket
import sys

# connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
msg = s.recv(1024)
print(msg.decode("utf-8"))


def msg_to_send():
    new_msg = input("Please enter the information you wish to request or Q to quit > ")
    if new_msg == "Q":
        print("BYE...")
        sys.exit(0)
    request = str.encode(new_msg)
    s.send(request)
    listenForMessages()


def listenForMessages():
    response = s.recv(1024)
    if response == "END":
        #sys.exit(0)
        msg_to_send()
    else:
        print(response.decode("utf-8"))
        listenForMessages()


msg_to_send()
