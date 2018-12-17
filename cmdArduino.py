from serial import Serial
import time
serial_port = Serial(port='/dev/cu.usbmodem143101',baudrate=9600)
if serial_port.isOpen():
	serial_port.close()
serial_port.open()

time.sleep(1)
lu = serial_port.readline()
chaine = lu.decode('ascii')
print(chaine)

serial_port.write(b'HELLO \r')

time.sleep(1)
lu = serial_port.readline()
chaine = lu.decode('ascii')
print(chaine)
print("entrer quit pour quitter")
while 1:
	commande = input("Entrez une commande : ")
	if commande=='quit':
		break
	
	commande +="\r"
	serial_port.write(commande.encode())



serial_port.close()


