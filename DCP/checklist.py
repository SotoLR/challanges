

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
	ignore_copied = True
	ignore_started = True
	ignore_done = True
	if copied != -1:
		#print("Checking copied ", copied)
		ignore_copied = False
	if started != -1:
		#print("Checking started ", started)
		ignore_started = False
	if done != -1:
		#print("Checking done ", done)
		ignore_done = False
	for line in data[1:]:
		#print(line)
		#print(f"Ignore copied:{ignore_copied} started:{ignore_started} done:{ignore_done}")
		#print(f"Values copied {int(line[1])}:{copied} started {int(line[2])}:{started} done {int(line[3])}:{done}")
		#print(f"Evaluations {ignore_copied or int(line[1])==copied} {ignore_started or int(line[2])==started} {ignore_done or int(line[3])==done}")
		if (ignore_copied or int(line[1])==copied) and (ignore_started or int(line[2])==started) and (ignore_done or int(line[3])==done):
			print(line)
			#print("=======PRINT THIS PRINT THIS PRINT THIS PRINT THIS PRINT THIS=======")
		#print("===")


#################
data = readFile("checklist.txt")

filter(data,started=0)