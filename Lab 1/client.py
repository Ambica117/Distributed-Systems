import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.56.1', 5000))

    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break
        response = client_socket.recv(1024).decode()
        print("Server:", response)

    client_socket.close()

start_client()
