


import re

## Open the logfile and read by the lines
def readFiles(filename):
	f = open(filename, "r")
	return(f.readlines())

## Clean it out to remove blank values
def removeBlanks(listobject):
	returnlist = []
	for i in listobject:
		if len(i) > 1:
			returnlist.append(i)
	return returnlist


## Main function to identify the vulnerable IP's
def regexPorts(fileObject):
	print("\n")
	ipHolder1 = ""
	ipHolder2 = ""
	# Declare empty Ports array that will get reinstantiated once a new IP is detected
	Ports = []

	step = 0
	while(step < len(fileObject)):
		try:
			## Set our values to compare with the current and next value
			## Starts out at the very first
			ipHolder1=fileObject[step]
			ipHolder2=fileObject[step+1]

			## Use Regex to separate the IP's and the Ports
			## Returns an array 
			search1 = re.search(r'(.*):(.*)', ipHolder1)
			search2 = re.search(r'(.*):(.*)', ipHolder2)


			## Get the IP and Port from the 1st Entry 
			ipRegex1 = search1.group(1)
			port1 = search1.group(2)


			## Get the IP and Port from the 2nd Entry 
			ipRegex2 = search2.group(1)
			port2 = search2.group(2)


			## By default our current IP for examination is the fileObject[step] entry
			## By default we want to append the port from the 1st Entry 
			Ports.append(port1)
			IPAddress = ipRegex1

			####
			## Once we find that the IP addresses for the current and next are not the same,
			if(IPAddress!=ipRegex2):

			## Print out what we have so far for our main IP Address on the Ports
				print("IPAddress ----> {}\n".format( IPAddress),  "Ports ----> {}\n".format( Ports))

			## Reset the values to equate to the next value ( which gets reset anyway on the next loop)
				checkForPortCount(Ports, IPAddress)
				IPAddress=ipRegex2
				Ports = []
			
		except:
			## Account for the very last value
			if(step==(len(fileObject)-1)):
				print("\nAt the Last Value\n")

				checkForPortCount(Ports, IPAddress)

				IPAddress=ipRegex2
				Ports = []
				Ports.append(port2)
				print("IPAddress ----> ", IPAddress,  " Ports:: \n", Ports)

		step+=1


## This function would need to be run right before 
## resetting either value of IPAddress and Ports
def checkForPortCount(arrayInput, IPAddressInput):
	if(len(arrayInput)>=3):
		print("ALERT::: MORE THAN 3 PORTS WERE SCANNED AT THIS IP ----> {}\n\n".format(IPAddressInput))
		return True
	return False


def main():
	ipAddressLines = readFiles("iplogs.txt")
	
	refinedIPAddressLines = removeBlanks(ipAddressLines)

	regexPorts(refinedIPAddressLines)

if __name__=="__main__":
	main()