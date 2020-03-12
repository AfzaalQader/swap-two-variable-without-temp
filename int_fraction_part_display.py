# Write a function which display the int part and fraction part of folat nummber,i.e if inout is 99.44.
# Output should be: "Interger part is: 99, Fractional Part is: 0.44" (String.split use ni krna)
def int_fraction_part(float_number):
	int_part = int(input_float_number)
	fractional_part = input_float_number % 1
	print('Integer Part is: {} , and Fractional Part is: {} '.format(int_part,round(fractional_part,2)))

if __name__ == "__main__":
	input_float_number = float(input('Enter float number:	'))
	int_fraction_part(input_float_number)

