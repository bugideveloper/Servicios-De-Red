import socket,pickle
from client_methods import *

archivos = get_archivos(".")
lista = pickle.dumps(archivos)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 8080))
client.send(lista)
from_server = client.recv(4096)
client.close()
print (from_server)



"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = ''
    while True:
        msg = s.recv(8)
        if len(msg) <= 0:
            break
        full_msg += msg.decode("utf-8")

    if len(full_msg) > 0:
        print(full_msg)
"""