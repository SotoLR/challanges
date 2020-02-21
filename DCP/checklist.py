

def main():
	data = readFile("checklist.txt")


def readFile(filename):	
	data = []
	with open(filename,"r") as f:
		for line in f:
			data.append([elem.strip() for elem in line.split(",")])
	return data

def printLine(line):
	print('{}\t{}\t{}\t'.format())

def filter(data, copied=-1,started=-1,done=-1):
	include_copied = True
	include_started = True
	include_done = True
	if copied == -1:
		copied = 0
		include_copied = False
	if started == -1:
		started = 0
		include_started = False
	if done == -1:
		done = 0
		include_done = False
	for line in data:
		if (include_copied and line[1]==str(copied)) and (include_started and line[2]==str(started)) and (include_done and line[3]==str(done)):
			#printLine(line)
			print(line)

#################
data = readFile("checklist.txt")
filter(data, 1,1,1)
print("=================")
filter(data, 1)