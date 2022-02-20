import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
# Port number can be anything between 0-65535 (we usually specify non-privileged ports which are > 1023)
s.listen(5)

while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} established")
    # f string is literal string prefixed with f which contains python expressions inside braces
    clt.send(bytes("Welcome from the basic python TCP server", "utf-8")) # To send info to client socket