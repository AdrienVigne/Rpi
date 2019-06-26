from servo import *
import socket

S1 = servo(12)
S2 = servo(16)

"""
try:
    while True:                      # Loop until Ctl C is pressed to stop.
        for dc in range(0, 101, 5):    # Loop 0 to 100 stepping dc by 5 each loop
            S1.rotation(dc)
            S2.rotation(dc)
            time.sleep(0.5)             # wait .05 seconds at current LED brightness
            print(dc)
        for dc in range(95, 0, -5):    # Loop 95 to 5 stepping dc down by 5 each loop
            S1.rotation(dc)
            S2.rotation(dc)
            time.sleep(0.5)             # wait .05 seconds at current LED brightness
            print(dc)
except KeyboardInterrupt:
    print("Ctl C pressed - ending program")
    S1.fin()
    S2.fin()
"""

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("192.168.1.62",35350))
print("Serveur d'écoute sur le port : ",353500)
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
