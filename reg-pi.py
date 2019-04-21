
 
from ipObject import ipObject 


def readFiles(filename):
	f = open(filename, "r")
	return(f.readlines())

def createObjects(filecontents):
	for i in filecontents:
		example = ipObject(i)
		print(example.address)

def main():
	print("hello world")
	filecontents = readFiles('iplogs.txt')
	createObjects(filecontents)

if __name__ == "__main__":
    main()
