import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.56.1', 5000))
    server_socket.listen(1)
    print("Server is listening on port 5000...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == 'exit':
            break
        print("Client:", data)
        response = input("Server: ")
        conn.send(response.encode())

    conn.close()

start_server()
