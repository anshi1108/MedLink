import socket
import threading

class VideoServer:
    def __init__(self):
        self.clients = {}
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('192.168.174.1', 9999))
        self.server.listen(1)
        print("Server listening on port 9999...")
        self.start_server()

    def handle_client(self, client_socket, addr):
        try:
            phone_number = client_socket.recv(1024).decode()
            self.clients[phone_number] = addr[0]
            print(f"Client {phone_number} connected from {addr[0]}:{addr[1]}")
        except Exception as e:
            print(f"Error handling client: {e}")

    def start_server(self):
        try:
            while True:
                client, addr = self.server.accept()
                client_handler = threading.Thread(target=self.handle_client, args=(client, addr))
                client_handler.start()
        except Exception as e:
            print(f"Error accepting client: {e}")

class VideoClient:
    def __init__(self, server_ip, server_port, phone_number, client_ip):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((server_ip, server_port))
            self.client.send(phone_number.encode())
        except Exception as e:
            print(f"Error connecting to server: {e}")

if __name__ == "__main__":
    server = VideoServer()

    client_ip = input("Enter the client's IP address: ")
    phone_number = input("Enter the client's phone number: ")

    client = VideoClient('127.0.0.1', 9999, phone_number, client_ip)
