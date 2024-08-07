# Exercise 3.13
"""Write a script that inputs a non-negative integer and computes and displays its factorial"""

#Prompt user to enter a number
number = int (input('Please enter non-negative number: '))

fact = 1
while number != 0:
    fact *= number
    number -= 1
print (fact)
