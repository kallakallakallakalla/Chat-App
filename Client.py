import socket

Server_Host = '0.0.0.0'
Server_Port = 55555
Client_Name = "Emilian"


def Start():
	socket_Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		socket_Client.connect((Server_Host, Server_Port))
		socket_Client.sendall(Client_Name)
		print("Verbindung erfolgt")
	except Exception as e:
		print(e)
		print("Verbindung nicht möglich...\nServer offline oder falsche IP/Port")
		print("iuabd")


def Nachricht_Senden(Nachricht, Empfänger):
	try:
		socket_Client.sendall(Nachricht + b"\n" + Empfänger)

	except Exception as e:
		print(e)
		print("Senden nicht möglich")


Start()
