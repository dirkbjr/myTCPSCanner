import socket, subprocess, sys
from datetime import datetime

#Ask for Input	

remoteServer = input("Enter a remote host to scan: ")
try:
	remoteServerIP = socket.gethostbyname(remoteServer)

except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	sys.exit()


openPorts = []


#Print banner with information on which host we are about to scan

print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)


#Check what time the scan started
t1 = datetime.now()

#Scan ports between 1 and 1024

try:
	for port in range(1,1024):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(10)

		result = sock.connect_ex((remoteServer, port))
		if result == 0:
			openPorts.append(port)
			print("Port{}:\t Open".format(port))
		else:
			print("Port{}:\t Closed".format(port))
		sock.close()

	for port in openPorts:
		print("Open: {}",port)

except KeyboardInterrupt:
	print("Exiting: Ctrl+C pressed")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved. Exiting")
	sys.exit()

except socket.error:
	print("Could not connect to server")
	sys.exit()


#Print all the data

t2 = datetime.now()

total = t2 - t1

print("Scanning Completed in: ", total)
