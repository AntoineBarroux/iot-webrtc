# Taken from:
# https://stackoverflow.com/questions/45364877/interpreting-keypresses-sent-to-raspberry-pi-through-uv4l-webrtc-datachannel
# based on:
# https://raspberrypi.stackexchange.com/questions/29480/how-to-use-pigpio-to-control-a-servo-motor-with-a-keyboard
# public domain

import socket
import time
import os 

socket_path = '/tmp/uv4l.socket'

try:
    os.unlink(socket_path)
except OSError:
    if os.path.exists(socket_path):
        raise

s = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)


print 'socket_path: %s' % socket_path
s.bind(socket_path)
s.listen(1)


while True:
    print 'awaiting connection...'
    connection, client_address = s.accept()
    print 'client_address %s' % client_address
    try:
        print 'established connection with', client_address


        while True:
            data = connection.recv(1024)
            print 'received message %s' % data
            time.sleep(0.01)
            if not data:
                #print 'echo data to client'
                #connection.sendall('hello ' + data)
#            else:
                print 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close()
