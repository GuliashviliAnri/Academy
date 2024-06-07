import socket
import threading

clients = []
def broadcast(message, curr_client):
    for client in clients:
        if client != curr_client:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(curr_client)


def handle(client_socket):
    while True:
        try:
            massage = client_socket.recv(1024)
            if massage:
                print(massage.decode())
                broadcast(massage.decode(), client_socket)

            else:
                client_socket.close()
                clients.remove(client_socket)
        except:
            client_socket.close()
            clients.remove(client_socket)
            break


def start(host="localhost", port=8088):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((host, port))
    server.listen()

    while True:
        client_socket, addr = server.accept()
        print(f"Connected {addr}")
        threading.Thread(target=handle, args=(client_socket,)).start()


start()
