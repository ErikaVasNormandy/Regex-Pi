
import sys
import re
from ossecObject import ossecAlert 


## Obtain the values
def parseThroughOSSEC(stringinput):
	ossecAlertArray = []
	for i in re.split(r'.*END OF NOTIFICATION.*', stringinput):
		ossecAlertHolder = ossecAlert(i)
		ossecAlertArray.append(ossecAlertHolder)
	return(ossecAlertArray)


def obtainReceived(ossecArray):
	for i in ossecArray:
		extractReceived = re.search(r'(Received): (.*)', i.raw_content)
		try:
			i.received = extractReceived.group(2)
		except:
			i.received = "No Receiver"
	return ossecArray

def obtainFrom(ossecArray):
	for i in ossecArray:
		extractMaterial = re.search(r'(Received From): (.*)->(.*)', i.raw_content)
		try:
			i._from = extractMaterial.group(3)
		except:
			i._from = "No Receiver"
	return ossecArray



def obtainAlertLevel(ossecArray):
	for i in ossecArray:
		extractAlertLevel = re.search(r'(Subject):(.*) - (.*) - (.*) (.*)', i.raw_content)
		try:
			i.alertLevel = extractAlertLevel.group(5)
		except:
			i.alertLevel = "No Alert Level"
			print("couldn't modify to alertLevel")
	return ossecArray


def obtainRule(ossecArray):
	for i in ossecArray:
		try:
			extractRule = re.search(r'(Rule):(.*)', i.raw_content)
			#extractRule = re.search(r'(Rule):(.*)(level .*)', i.raw_content)
			i.rule = extractRule.group(2)
		except:
			i.rule = "No Rule identified"
	return ossecArray

def obtainDate(ossecArray):
	for i in ossecArray:
		extractMaterial = re.search(r'(Date): (.*), (.*)', i.raw_content)
		try:
			i.date = extractMaterial.group(3)
		except:
			i.date = "No date"
	return ossecArray


def obtainLogContent(ossecArray):
	for i in ossecArray:
		extractMaterial = re.search(r'(Portion)(.*)\n\n(.*)', i.raw_content)
		try:
			i.logcontent = extractMaterial.group(3)
		except:
			i.logcontent = "No Receiver"
	return ossecArray


def main():
    f = open("example.txt","r")
    stringFile = f.read()
    arrayoutput = parseThroughOSSEC(stringFile)
    arrayoutput = obtainAlertLevel(arrayoutput)
    obtainRule(arrayoutput)
    obtainReceived(arrayoutput)
    obtainFrom(arrayoutput)
    obtainDate(arrayoutput)
    obtainLogContent(arrayoutput)


    for i in arrayoutput:
    	print("\n\nAlert Level of: ", i.alertLevel)
    	print("Received On: ", i.date)
    	print("Source is: ", i.received)
    	print("Filepath is: ", i._from)
    	print("-------------")
    	print("Rule Level is: ", i.rule)
    	print("-------------")

    	print("Message::::\n", i.logcontent)
    	print("\n")
    	print("-------------------------------------")

    	print("-------------------------------------")




if __name__ == "__main__":
    main()
