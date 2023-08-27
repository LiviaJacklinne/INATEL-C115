import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print(data)
        response = input().strip().lower()
        client_socket.sendall(response.encode())

    client_socket.close()

if __name__ == "__main__":
    main()