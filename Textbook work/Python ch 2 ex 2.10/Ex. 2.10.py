#Exercise 2.10
""" (Arithmatic, Smallest and Largest)  Write a script that inputs three integers from the user.  Display the sum, average, product, smallest and largest of the numbers"""

#Prompt user to enter 3 numbers
num1 = int (input('Please enter the first number: '))
num2 = int (input('Please enter the second number: '))
num3 = int (input('Please enter the third number: '))

#Calculate the sum of the numbers and display
print('The sum of the three numbers entered is: ', num1 + num2 + num3)

#Calculate the product of the numbers and display
print("The product of the three numbers entered is: ", num1 * num2 * num3)

#Find and display the smallest of the three numbers
min = num1

if num2 < min:
    min = num2

    if num3 < min:
        min = num3

print ('The smallest number entered was: ', min)

#Find and display the largest of the three numbers
max = num1
if num2 > max:
    max = num2

    if num3 > max:
        max = num3

print ('The largest number entered was: ', max)