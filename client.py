import socket

def client_connect(host, port):
    sock = socket.socket()
    sock.setblocking(1)
    sock.connect((host, port))
    print(f"Соединение с сервером {host} установлено на порту {port}")

    try:
        while True:
            msg = input('Введите строку: ')
            
            print("Отправка данных серверу")
            sock.sendall(msg.encode())

            if msg.lower() == 'exit':
                print('Разрыв соединения с сервером')
                break

            data = sock.recv(1024)
            print("Прием данных от сервера: ", data.decode())

    finally:
        sock.close()


client_connect('192.168.0.17', 9090)