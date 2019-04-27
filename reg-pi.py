
 
from ipObject import ipObject 
import re

def readFiles(filename):
	f = open(filename, "r")
	return(f.readlines())


def getIPs(stringinput):
	search = re.search(r'(.*):(.*)', stringinput)
	ipaddress = search.group(1)
	port = search.group(2)
	return(ipaddress)

def separatePorts(stringinput):
	search = re.search(r'(.*):(.*)', stringinput)
	ipaddress = search.group(1)
	port = search.group(2)
	return({ipaddress:port})


def createObjects(filecontents):
	arrayToReturn = []
	for line in filecontents:
		if(len(line)>1 ):
			ipaddress = getIPs(line)
			emptyIPObject = ipObject(ipaddress)	
			arrayToReturn.append(emptyIPObject)
		elif():
			print("empty value")
	return arrayToReturn


def getPorts(fileInput, arrayInput):
	for ipObject in arrayInput:
		for line in fileInput:
			try:
				ipaddress = separatePorts(line)
				# print(ipaddress)
						###{'192.168.1.1': '21'}
						###{'192.168.1.1': '80'}
						###{'192.1.1.4': '39'}
				for i in ipaddress:
					# print(i)
					# print(ipObject.address, " versus ", i)
					if(ipObject.address==i):
						print("FOUND")
						print(ipObject.address, " ", i)
						ipObject.setPorts(ipaddress[i])

			except:
				continue;



def checkContents(arrayInput):
	for i in arrayInput:
		print("\n", i, " ::::: ")
		try:
			print("Has an IP address of ---------> ", i.address)
			print("Has ports of ---------> ", i.ports)
			print("alarm? ---------> ", i.alarm)

		except:
			print("unable to, error occurred")


# def removeDuplicateIPsAndSetPorts(arrayInput):
# 	for ipObject in arrayInput:



def main():
	filecontents = readFiles('iplogs.txt')
	arrayOfIPObjects = createObjects(filecontents)
	getPorts(filecontents, arrayOfIPObjects)


	checkContents(arrayOfIPObjects)
	# separatePorts(arrayOfIPObjects)
	# for i in arrayOfIPObjects:
	# 	i.createPorts()

if __name__ == "__main__":
    main()
