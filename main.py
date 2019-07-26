from servo import *
import socket

S1 = servo(12)
S2 = servo(16)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try :
    sock.bind(("192.168.1.33",35351))
except :
    sock.close()
    sock.bind(("192.168.1.33",35351))
print("Serveur d'écoute sur le port : ",35351)
sock.listen(5)
print("attente connexion")
connexion,adresse=sock.accept()
print("client conneté ip : %s, port : %s",adresse[0],adresse[1])
while 1 :
    msg = connexion.recv(1024)
    msg = msg.decode()
    if msg == 'q':
        connexion.close()
        sock.close()
        break
    if msg == 'up':
        S1.set_angle(1)
    if msg == 'down':
        S1.set_angle(-1)
    if msg == 'right':
        S2.set_angle(1)
    if msg == 'left':
        S2.set_angle(-1)
