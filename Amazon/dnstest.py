from socket import gethostbyaddr
import ipcalc
import time

#Took the below function from http://small-code.blogspot.com/2008/05/nslookup-in-python.html
#props to that guy this.is.lance.miller@gmail.com
def nslooky(ip):
	try: 
		output = gethostbyaddr(ip)
		return output[0]

	except: 
		output = "not found" 
		return output


#Open file
f = open('prefixes.txt', 'r')

#For loop that pulls each subnet out of the file
for val in f.readlines():

        #For loop to print every ip address in the subnet.
        for ip in ipcalc.Network(val.strip()):
		fqdn = nslooky(str(ip))
		print str(ip) + ' ' + fqdn
		time.sleep(5)
