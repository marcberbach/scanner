#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

remoteServer	= input("Enter a remote host to scan: ") or "192.168.254.254"
remotePorts		= input ("TCP ports list comma separated, default 22,80,110,443,445,8080 : ") or "22,80,110,443,445,8080"
remoteServerIP  = socket.gethostbyname(remoteServer)

print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

try:
	for port in (map(int, remotePorts.split(','))):  
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1.0)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print ("Port {}: 	 Open".format(port))
		sock.close()

except KeyboardInterrupt:
	print ("You pressed Ctrl+C")
	sys.exit()

except socket.gaierror:
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

except socket.error:
	print ("Couldn't connect to server")
	sys.exit()
