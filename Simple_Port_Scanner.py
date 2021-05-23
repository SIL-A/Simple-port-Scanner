#This is just a simple program. It's not designed to do sophesticated things like verbose scanning. 

import socket

q = input("Enter the website's name or IP address: \n")
y = int(input("\nEnter the range of port you want to scan: \n"))
try:
	x = socket.gethostbyname(q)
except socket.gaierror:
	print("\nInvalid Hostname. Exiting .......\n")
	quit()
try:
	for i in range(1, y):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((x, i))
		if result==0:
			print("Port {} is open".format(i))
		s.close()
except KeyboardInterrupt:
	print("\nExiting due to keyboard interrupt .......\n")
	quit()
except socket.error:
	print("\nServer not responding. Exiting ....... \n")
	quit()
except:
	print("\nSome error has occurred. Exiting .......\n")
