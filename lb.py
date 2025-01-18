import socket
import threading

HOST = "127.0.0.1"
PORT = 4321

class Server:

    def client_connection(self, conn, addr):
        with conn:
            print(f"Connected by {addr}")

            buffer = ""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                buffer += data.decode('utf-8')
                print(f"Message: {buffer}")
            

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((HOST, PORT))
        self.socket.listen()

        print(f"Server is running on {HOST}:{PORT}")

        while True:
            conn, addr = self.socket.accept()

            t = threading.Thread(target=self.client_connection, args=(conn, addr))
            t.start()


if __name__ == "__main__":
    server = Server()
            



