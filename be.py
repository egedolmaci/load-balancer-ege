from lb import Server
import socket
import threading

HOST = "127.0.0.1"
PORT = 5432

class BackendServer(Server):
    def __init__(self, backend_host, backend_port):
        # Don't need to pass backend parameters to load balancer's init
        super().__init__(backend_host, backend_port, "", 0)
    
    def forward_requests(self, client_conn, client_addr):
        try:
            data = client_conn.recv(1024)
            if data:
                print(data)
                response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nResponse from backend server"
                client_conn.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Error handling request: {e}")
        finally:
            client_conn.close()

if __name__ == "__main__":
    server = BackendServer(HOST, PORT)
    server.start()