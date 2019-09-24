import socket


def Start():
	Server_Host = "127.0.0.1"
	Server_Port = 55555

	try:
		socket_Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket_Client.bind((Server_Host, Server_Port))
		socket_Client.listen()
		print("Server wartet auf Verbindung...")
		conn, addr = s.accept()
		Empfange_Daten(conn, addr)
	except Exception as e:
		print(e)
		print("Server konnte nicht hochgefahren werden... \nFalsche IP oder Port ")


def Empfange_Daten(conn, addr):
	i = 0
	with conn:

		while True:
			Nachricht = conn.recv(1028)

			if i == 0:
				print("Verbindung erfolgt mit Client : " + Nachricht)
				i + 1

			if not Nachricht:
				break


Start()
