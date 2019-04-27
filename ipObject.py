
import re

class ipObject:
	
	def __init__(self, addressInput):
		self.address = addressInput
		self.ports = []
		self.alarm = False
	 
	def getAddress(self):
		return self.address


	def createPorts(self):
		result = re.search(r'(.*):(.*)', self.address)
		result3example = re.search(r'(.*):(3*)', self.address)

		print(self.address, result.group(2), "\n", result3example.group(2))


	def setAlarm(self):
		if(len(self.ports))>=2:
			return True
		else:
			return False

	def setPorts(self, portInput):
		self.ports.append(portInput)
		self.setAlarm()


		