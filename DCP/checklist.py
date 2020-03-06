

def main():
	data = readFile("checklist.txt")
	print("\t1) Print all")
	print("\t2) Print started, not done")
	print("\t3) Print done")
	print("\t4) Print copied")
	print("\t5) Custom filter")
	print("\t6) Edit item")
	opt = -1
	while True:
		opt = int(input(">"))
		if opt<0 or opt>6:
			print("====== Invalid option ======")
		else:
			break
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
		editEntry(len(data))



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

def editEntry(data_len):
	while True:
			try:
				entry_id = int(input(f"# of entry to change (4-{data_len}): "))
				if entry_id > 3 and entry_id < data_len-1:
					break
				else:
					print(f"Invalid entry: {entry_id} is outside of the range of problems (4-{data_len}).")
			except ValueError:
				print(f"Invalid entry: {entry_id} is not recognized as a number.")
			print("Please try again.\n")

#################
main()
