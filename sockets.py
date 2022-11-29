import socket
from concurrent.futures import ThreadPoolExecutor

import orjson

HOST = '127.0.0.1'
PORT = 65335


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Connected to {addr}')
            while True:
                data = conn.recv(1024)
                conn.sendall(data)


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            s.sendall(orjson.dumps(input()))
            data = s.recv(1024)
            print(data)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        [executor.submit(target) for target in (server, client)]
