import json
import socket

## https://www.askpython.com/python/dictionary/convert-json-to-a-dictionary

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
# Port number can be anything between 0-65535 (we usually specify non-privileged ports which are > 1023)
s.listen(5)

while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} established")
    # f string is literal string prefixed with f which contains python expressions inside braces
    clt.send(bytes("Welcome from the basic python TCP server", "utf-8")) # To send info to client socket

    # with open('../results.json') as json_file:
    #     data = json.load(json_file)

    file = open("resources/results.json", 'r')
    json_data = json.load(file)

    searched = s.recv(adr)
    for test in json_data:
        if test['Test Number'] == searched:
            for i in test:
                print(i)

