import gc
gc.collect()

from utime import localtime
import network
SSID="<SSID-NAME>"
PASSWORD="<PASSWORD>"
IP="192.168.5.1"
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, authmode=3, password=PASSWORD)
ap.ifconfig((IP,'255.255.255.0',IP,'8.8.8.8'))

print("AP OK")

import socket
from machine import RTC

port = 80
listenSocket = None


ip = ap.ifconfig()[0]
listenSocket = socket.socket()
try:
  listenSocket.bind((ip, port))
except:
  print("already binded")
listenSocket.listen(5)
listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,  1)
RED.on()

while True:
    print("accepting.....") 
    conn, addr = listenSocket.accept()
    print(addr, "connected")

    while True:
        data = conn.recv(1024)
        if(data.decode()=="end"):
          print("close socket")
          conn.close()
          RED.off()
          sys.exit(0)
        if(len(data) == 0):
          print("close socket")
          conn.close()
          break
        print(data.decode()+"\n")
        with open("log.txt","a") as f:
          f.write("{4:02d}:{5:02d}:{6:02d}:{7:06d}".format(*RTC().datetime()))
          f.write(",")
          f.write(str(data.decode())+"\n")
          
