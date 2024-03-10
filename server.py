import socket
import threading

from settings import HOST, PORT, logging
from static.static import get_static_by_request
from urls import UrlDispatcher


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.url_dispatcher = UrlDispatcher()

    def run_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)

            logging.info(f'http://{self.host}:{self.port}')

            while True:
                try:
                    client_socket, client_address = server_socket.accept()
                    request = client_socket.recv(1024).decode('UTF-8')

                    if request.startswith('POST'):
                        request += client_socket.recv(1024).decode('UTF-8')

                    if not request:
                        continue

                    logging.info(request)

                    thread = threading.Thread(target=self.handle_request, args=(client_socket, request))
                    thread.start()

                except Exception as e:
                    logging.error(f'Error handling request: {e}')

    def handle_request(self, client_socket, request):
        if request.startswith('GET /static/'):
            static = get_static_by_request(request)
            client_socket.sendall(static)
        else:
            template = self.url_dispatcher.get_template_by_request(request)
            client_socket.sendall(template)

        client_socket.shutdown(socket.SHUT_WR)


if __name__ == '__main__':
    server = Server(HOST, PORT)
    server.run_server()
