# Taken from:
# https://stackoverflow.com/questions/45364877/interpreting-keypresses-sent-to-raspberry-pi-through-uv4l-webrtc-datachannel
# based on:
# https://raspberrypi.stackexchange.com/questions/29480/how-to-use-pigpio-to-control-a-servo-motor-with-a-keyboard
# public domain

import socket
import time
import os
import json
import re
from serial import Serial
 

socket_path = '/tmp/uv4l.socket'
serial_port = '/dev/ttyACM0'

serial_port = Serial(port=serial_port, baudrate=9600)
if serial_port.isOpen():
	serial_port.close()
serial_port.open()
lu = serial_port.readline()
chaine = lu.decode('ascii')
print(chaine)

try:
    os.unlink(socket_path)
except OSError:
    if os.path.exists(socket_path):
        raise

s = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)


print ('socket_path: %s' % socket_path)
s.bind(socket_path)
s.listen(1)


while True:
    print ('awaiting connection...')
    connection, client_address = s.accept()
    print ('client_address %s' % client_address)
    try:
        print ('established connection with', client_address)
        delta = None


        while True:
            data = connection.recv(1024)

            if not data:
                print ('no more data from', client_address)
                break

            try:
                json_object = json.loads(data.decode())
                print(json_object["do"])
                gamma = abs(json_object["do"]["gamma"])
                top = int(-1.0889 * gamma + 109)
                command = "T " + str(top) + "\r";
                serial_port.write(command.encode())
                alpha = json_object["do"]["alpha"]
                if delta == None:
                    delta = 90 - int(alpha)
                command = "L " + str((alpha + delta)%180) + "\r";
                print(command)
                serial_port.write(command.encode())
            except ValueError as e:
                expression = "^(T|L) \d+"
                commande = data.decode()
                if re.match(expression, commande):
                    print(commande)
                    commande +="\r"
                    serial_port.write(commande.encode())
                
      

    finally:
        # Clean up the connection
        connection.close()
