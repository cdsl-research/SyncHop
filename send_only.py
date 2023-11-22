import gc
gc.collect()

from utime import sleep,localtime

import network
if "wifi" in locals():
  wifi.active(False)
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

import socket
from machine import Timer,RTC

s = socket.socket()
host = '192.168.5.1'
port = 80

s.connect(socket.getaddrinfo(host, port)[0][-1])
print("Socket Connected")


#while True:
#  msg = input("--->>> ")
#  s.sendall(msg)

def t0_callback(t):
  msg = b'0.12345'
  s.sendall(msg)
  print(msg)
  with open("log.txt","a") as f:
    f.write("{4:02d}:{5:02d}:{6:02d}:{7:06d}".format(*RTC().datetime()))
    f.write(",")
    f.write(msg.decode())
    f.write(",")
    f.write(str(wifi_STA.status("rssi")))
    f.write("\n")

t0 = Timer(0)
t0.init(period=10000,mode=t0.PERIODIC,callback=t0_callback)

sleep(3600)
t0.deinit()

#try:
#  for i in range(3):  
#    s.sendall(b'end')
#    sleep(0.1)
#except:
#  print("end")
