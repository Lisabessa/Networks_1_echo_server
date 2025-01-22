import socket

def run_echo_server(host, port):
	print(f"Сервер запущен на хосте {host}, используя порт {port}")
	sock = socket.socket()
	sock.bind((host, port))
	sock.listen(1)


	print("Начало прослушивания порта")
	while True:
		conn, addr = sock.accept()
		print(f"Подключение клиента {addr}")

		try:
			while True:
				data = conn.recv(1024)

				if not data:
					print(f"Отключение клиента {addr}")
					break

				print(f"Прием данных от клиента: {data.decode()}")
				print("Отправка данных клиенту")
				conn.sendall(data)
		finally:
			sock.close()
			print("Сервер остановлен")
			break


run_echo_server('', 9090)