# Excercise 2.6
""" (Odd or even) Use 'if' statement to determine whether an integer is odd or even."""

#Prompt user to input an integer
num = int (input('Please enter a number: '))

check = num % 2

if check == 0:
	print ('Number is even!')
else:
	print ('Number is odd!')