import socket

def receive():
    while True:
        try:
            message = client_socket.recv(1024)
            if massage:
                print(message.decode())
            else:
                break
        except:
            break


def client(host="localhost", port=8088):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("Type your name: ")
    client_socket.send(message.encode())

    # threading.Thread(target=receive, args=(client_socket, )).start()

    while True:
        message = input()
        if massage == "quit":
           client_socket.close()
           break
        client_socket.send(message.encode())


client()