import socket


class ClientException(Exception):
    pass


class Client:
    def __init__(self, address, port, timeout=None):
        self.address = address
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((address, port), timeout=timeout)
        except socket.error as err:
            raise ClientException('Невозможно установить соединение', err)

    def get(self):
        pass

    def put(self):
        pass
    
    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientException('Невозможно закрыть соединение', err)


if __name__ == '__main__':
    pass
