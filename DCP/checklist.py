

def main():
	data = readFile("checklist.txt")
	print("\t1) Print all")
	print("\t2) Print started, not done")
	print("\t3) Print done")
	print("\t4) Print copied")
	print("\t5) Custom filter")
	print("\t6) Edit item")
	opt = getNumOptionInput(">",1,6)
	if opt == 1:
		printLine(data[0])
		filter(data)
	elif opt == 2:
		printLine(data[0])
		filter(data, started=1, done=0)
	elif opt == 3:
		printLine(data[0])
		filter(data, done=1)
	elif opt == 4:
		printLine(data[0])
		filter(data, copied=1)
	elif opt == 5:
		print("Under construction")
		opt = 0
		while opt != 0 and opt != 1:
			pass
		#opt = -1
		while opt != 0 and opt != 1:
			pass
		#opt = -1
		while opt != 0 and opt != 1:
			pass
	elif opt == 6:
		editEntry(data)



def readFile(filename):	
	data = []
	with open(filename,"r") as f:
		for line in f:
			data.append([elem.strip() for elem in line.split(",")])
	return data

def printLine(line):
	print('{}\t{}\t{}\t{}'.format(line[0], line[1], line[2], line[3]))
	"""
	if line[0]=='#':
		print('{}\t{}\t{}\t{}'.format(line[0], line[1], line[2], line[3]))
	else:
		print('{}\t{}\t{}\t{}'.format(line[0], int(line[1])==1, int(line[2])==1, int(line[3])==1))
	"""


def filter(data, copied=-1,started=-1,done=-1):
	result_count = 0
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
			printLine(line)
			result_count += 1
			#print("=======PRINT THIS PRINT THIS PRINT THIS PRINT THIS PRINT THIS=======")
		#print("===")
	print("========= {} Results found =========".format(result_count))

def editEntry(data):
	start_index = 3
	data_len = len(data)

	entry_id = getNumOptionInput("# of entry to change ({}-{}): ".format(start_index+1, data_len-start_index), start_index, data_len-start_index)
	print()
	printLine(data[0])
	printLine(data[entry_id - start_index])
	print()
	print("\t1) Set as 'Not copied'")
	print("\t2) Set as 'Copied'")
	print("\t3) Set as 'Started'")
	print("\t4) Set as 'Done'")
	print("\t5) Cancel change")
	selection = getNumOptionInput(">",1,5)
	print(selection)
	#TODO: Test that all works well so far
	#Edit entry based on input
	value_dict = {
		1: [0,0,0],
		2: [1,0,0],
		3: [1,1,0],
		4: [1,1,1]
	}

	#Maybe change condition to selection!=5 and simply return if Canceled?
	if selection == 5:
		#Canceled
	else:
		value_dict.get(selection)



def getNumOptionInput(prompt,minval,maxval):
	opt = minval - 1
	while True:
		try:
			opt = int(input(prompt))
			if opt<minval or opt>maxval:
				print(f"====== Invalid option: {opt} is out of range ({minval}-{maxval}) ======")
			else:
				break
		except ValueError:
			print(f"====== Invalid entry: {entry_id} is not recognized as a number ======")
	return opt

#################
main()
