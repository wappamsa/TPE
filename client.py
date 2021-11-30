import socket

host, port = ('localhost', 4848)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("client connecté!")

    data = "Bonjour, moi c'est WAPPAMSA BOUBA GILDAS !"
    data = data.encode("utf8")
    socket.sendall(data)
except:
    print("Connexion au serveur échoué !")
finally:
    socket.close()
