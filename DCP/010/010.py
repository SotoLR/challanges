import time

def callfunc(func, delay):
	calltime = time.time()*1000
	while((time.time()*1000)-calltime < delay):
		pass
	func("AAAA")

def myfunc(text):
	print(text)

callfunc(myfunc, 10000)