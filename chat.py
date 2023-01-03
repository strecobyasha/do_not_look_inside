from pydantic import BaseSettings
import socket
import threading


class Settings(BaseSettings):
    host: str = '127.0.0.1'
    port: str = '7976'

    class Config:
        env_file = '.env'


settings = Settings()


class Server:

    def __init__(self):
        self.clients = []
        self.pseudonyms = []

    def serve_forever(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
            listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            listen_socket.bind((settings.host, int(settings.port)))
            listen_socket.listen()

            while True:
                client_connection, client_address = listen_socket.accept()
                print('Connected with {}'.format(str(client_address)))
                client_connection.send('Connected'.encode('ascii'))
                pseudonym = client_connection.recv(1024).decode('ascii')
                self.pseudonyms.append(pseudonym)
                self.clients.append(client_connection)
                print('Nickname is {}'.format(pseudonym))
                self.broadcast('{} joined'.format(pseudonym).encode('ascii'))
                thread = threading.Thread(target=self.handle, args=(client_connection,))
                thread.start()

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while True:
            message = client.recv(1024)
            self.broadcast(message)


class Client:

    def __init__(self):
        self.pseudonym = input('Choose your pseudonym: ')
        self.client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_connection.connect((settings.host, int(settings.port)))

    def receive(self):
        while True:
            try:
                message = self.client_connection.recv(1024).decode('ascii')
                if message == 'Connected':
                    self.client_connection.send(self.pseudonym.encode('ascii'))
                else:
                    print(message)
            except:
                print('An error occured!')
                self.client_connection.close()
                break

    def write(self):
        while True:
            message = '{}: {}'.format(self.pseudonym, input(''))
            self.client_connection.send(message.encode('ascii'))
