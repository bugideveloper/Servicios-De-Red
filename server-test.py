
import socket,pickle
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((socket.gethostname(), 8080))
serv.listen(5)

print("Server ready to get connection")
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        archivos = pickle.loads(data)
        for archivo in archivos:
            print(archivo)
        conn.send(bytes("I am SERVER<br>","utf-8"))
    conn.close()
    print('client disconnected')

"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    clientsocket.close()
"""