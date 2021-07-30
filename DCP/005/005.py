def cons(a,b):
	def pair(f):
		return f(a,b)
	return pair

def car(f):
	def print_first(a,b):
		return a
	return f(print_first)

def cdr(f):
	def print_second(a,b):
		return b
	return f(print_second)


print(car(cons(3,4)))
print(cdr(cons(3,4)))