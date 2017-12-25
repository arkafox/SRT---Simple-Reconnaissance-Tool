"""

Simple reconnaissance tool
Feel free to change the code or give opinions.

arkafox@protonmail.com

-ArkaFox 2017

"""

import socket
import subprocess
import sys
from colors import *
import os

ban = "Simple Reconnaisance Tool 1.0\nArkaFox 2017\nFeel free to change the code or give opinions."
bar = "-" * 30

def Bannergrab(ip,port):

	try:

		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner

	except Exception, e:

		if "Connection refused" in str(e):
			print "Port closed, the connection was refused"
			char = raw_input("Press any key to continue")
			subprocess.call("clear",shell=True)
			main()

	except KeyboardInterrupt:
		print "Quitting..."
		sys.exit(0)

def Portscan(ip):

	try:

		for port in range(1,65000):
			socket.setdefaulttimeout(2)
			s = socket.socket()
			connection = s.connect_ex((ip,port))
			if connection == 0:
				print "[+] Port %d -> Open" % port
			s.close()

	except Exception,e:
		print str(e) 
		sys.exit(0)


	except (KeyboardInterrupt, SystemExit):
        	print "\nQuitting..."
        	sys.exit(0)

	except socket.error:
		print "\nCouldn't connect to server"
		sys.exit(0)

def main():
	
	sys.stdout.write(GREEN)
	print ban
	print bar
	option = raw_input("What do you want to do?\n\n\nBannergrab [1]\nPortscan [2]\nQuit [0]\n\n\nOption: ")
	if option == "1":
		print bar
		ip = raw_input("IP: ")
		print bar
		port = int(raw_input("Port: "))
		print bar
		banner = Bannergrab(ip,port)
		if banner:
			print banner
			cont = raw_input("\nPress any key to continue. \n")
			main()


	elif option == "2":

		print bar
		ip = str(raw_input("IP: "))
		print bar
		Portscan(ip)
		try:

			cont = raw_input("\nPress any key to continue. [CTRL^C to quit] \n")
			main()
		except (KeyboardInterrupt,SystemExit):
			print "\nQuitting..."
			sys.exit()
	elif option == "0":
		print "Thank you for using Simple Reconnaisance!\nQuitting..."
		sys.exit(0)

	else:
		print "Invalid option!\nPress any key to choose again or press [CTRL+C] to quit."
		char = raw_input("")
		subprocess.call("clear",shell=True)
		main()


if __name__ == '__main__':
	main()
