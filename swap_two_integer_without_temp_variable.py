# Write a function which swaps the two integers without 3rd varibale
# We can sovle this by using sum method 

def swap(x,y):
	x = x + y
	y = x - y    # value of x is assign to variable y
	x = x - y    # value of y is assign to variable y
	print("Value of x is : {} , Value of Y is : {}".format(x,y))

def swap_using_multiplication(x,y):
	x = x * y
	y = x / y
	x = x / y
	print("Value of x is : {} , Value of Y is : {}".format(int(x),int(y)))

if __name__ == "__main__":
	x = int(input('Enter the first number:	'))
	y = int(input('Enter the second number:	'))
	swap_using_multiplication(x,y)