import math as Math

def func(x):
	return (x**3 - 32*x + 8)

def muller_method(x0,x1,x2,allow_error):
	iteration = 0    
	while(1):
		h0 = x1 - x0
		h1 = x2 - x1

		del0 = (func(x1) - func(x0))/h0
		del1 = (func(x2) - func(x1))/h1

		a = (del1 - del0)/(h0 + h1)
		b = a*h1 + del1
		c = func(x2)

		if(b < 0):
			x3 = x2 + ((-2)*c)/(b - Math.sqrt((b**2) - (4*a*c)))
			print("Iteration ",iteration, ": ", x3)
		else:
			x3 = x2 + ((-2)*c)/(b + Math.sqrt((b**2) - (4*a*c)))
			print("Iteration ",iteration, ": ", x3)

		calculated_error = (x2 - x3)/x3

		if(calculated_error <= allow_error):
			return x3
		else:
			x0 = x1
			x1 = x2
			x2 = x3
		iteration += 1

def main():

	print("Initital Value for x0 : ")
	x0 = float(input())
	print("Initital Value for x1 : ")
	x1 = float(input())
	print("Initital Value for x2 : ")
	x2 = float(input())

	print("Error: ")
	allow_error = float(input())

	root_x = muller_method(x0, x1, x2, allow_error)
	
	print("Root: ", root_x)
	print("Evaluation: ", func(root_x))


main()
