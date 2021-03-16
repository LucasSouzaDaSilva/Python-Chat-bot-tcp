import threading
import socket

host = '127.0.0.3'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nickname = []

def broadcast():
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = [index]
            broadcast('{} deixou o chat'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        # Aceitar a conexão
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname do client é {}".format(nickname))
        broadcast("{} entrou no chat!".format(nickname).encode('ascii'))
        client.send('Conectado ao servidor!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()

