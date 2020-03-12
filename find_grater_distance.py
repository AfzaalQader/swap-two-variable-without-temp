# input two distance form the user in feet and inches, print the grater distance.
# i.e (12 feet, 8 inches)  (10 feet, 11 inches)

def grater_distance(distance_1_in_feet,distance_1_in_inches,distance_2_in_feet,distance_2_in_inches):
	if distance_1_in_feet == distance_2_in_feet:
		if distance_1_in_inches == distance_2_in_inches:
			print('Both distance are equal')
		elif distance_1_in_inches > distance_2_in_inches:
			print('{} feet , {} inches'.format(distance_1_in_feet,distance_1_in_inches))
		else:
			print('{} feet , {} inches'.format(distance_2_in_feet,distance_2_in_inches))
	elif distance_1_in_feet > distance_2_in_feet:
		print('{} feet , {} inches'.format(distance_1_in_feet,distance_1_in_inches))
	else:
		print('{} feet , {} inches'.format(distance_2_in_feet,distance_2_in_inches))

if __name__ == "__main()__":
	distance_1_in_feet = int(input('Enter distance 1 in feet:	'))
	distance_1_in_inches = int(input('Enter distance 1 in Inches:	'))

	distance_2_in_feet = int(input('Enter distance 2 in feet:	'))
	distance_2_in_inches = int(input('Enter distance 2 in inches:	'))

	grater_distance(distance_1_in_feet,distance_1_in_inches,distance_2_in_feet,distance_2_in_inches)

