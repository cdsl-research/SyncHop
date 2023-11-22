import gc
gc.collect()

from utime import localtime
import network
SSID="<SSID-NAME>"
PASSWORD="<PASSWORD>"
IP="<IP-ADDRESS>"
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

if "wifi_STA" in locals():
  wifi_STA.active(False)
SSID_NAME="<SSID-NAME>"
SSID_PASS="<PASSWORD>"
def connect_wifi(ssid, passkey, timeout=10):
    wifi_STA = network.WLAN(network.STA_IF)
    if wifi_STA.isconnected():
        print('already Connected.    connect skip')
        return wifi_STA
    else:
        wifi_STA.active(True)
        wifi_STA.connect(ssid, passkey)
        while not wifi_STA.isconnected() and timeout > 0:
            print('.')
            timeout -= 1
    if wifi_STA.isconnected():
        print('Connected')
        return wifi_STA
    else:
        print('Connection failed!')
        return null


wifi_STA = connect_wifi(SSID_NAME, SSID_PASS)

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
        s = socket.socket()
        host = '192.168.5.1'
        port = 80
        
        s.connect(socket.getaddrinfo(host, port)[0][-1])
        print("Socket Connected")
        s.sendall(msg)
