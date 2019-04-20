
 

def readFiles(filename):
	f = open(filename, "r")
	print(f.read())



def main():
	print("hello world")
	readFiles('iplogs.txt')


if __name__ == "__main__":
    main()
