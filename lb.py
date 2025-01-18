import socket
import threading

HOST = "127.0.0.1"
PORT = 4321

class Server:
    
    def __init__(self, lb_host, lb_port, backend_host="", backend_port=0):
        self.lb_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lb_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.lb_socket.bind((lb_host, lb_port))
        self.lb_socket.listen()

        print(f"Server is running on {lb_host}:{lb_port}")

        self.backend_host = backend_host
        self.backend_port = backend_port

    def forward_requests(self, client_conn, client_addr):
        backend_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            backend_socket.connect((self.backend_host, self.backend_port))


            data = client_conn.recv(1024)
            if data:
                print(data.decode())
                backend_socket.sendall(data)


                response = backend_socket.recv(1024)
                print(response)

                client_conn.sendall(response)

        except Exception as e:
            print(f"Error forwarding request: {e}")
            

    def start(self):
        while True:
            client_conn, client_addr = self.lb_socket.accept()
            print(f"Client connected from {client_addr}")

            t = threading.Thread(target=self.forward_requests, args=(client_conn, client_addr))
            t.start()

            



if __name__ == "__main__":
    client_port = 4321
    client_addr = "127.0.0.1"
    backend_port = 5432
    backend_addr = "127.0.0.1"
    
    server = Server(client_addr, client_port, backend_addr, backend_port)
    server.start()
            



