import socket
import sys

# connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
msg = s.recv(1024)
print(msg.decode("utf-8"))
looper = False


def msg_to_send():
    new_msg = input("Please enter the information you wish to request or Q to quit > ")
    if new_msg == "Q":
        print("BYE...")
        sys.exit(0)
    bytes_to_send = str.encode(new_msg)
    return bytes_to_send


def main():
    request = msg_to_send()
    s.send(request)
    response = s.recv(1024)
    print(response.decode("utf-8"))


# while not looper:
#     main()

main()
