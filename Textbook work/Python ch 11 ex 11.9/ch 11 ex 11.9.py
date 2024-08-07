#(Greatest common Divisor) Write and test a recursive function that returns the greatest common divisor of x and y.
#Establish empty lists to store the divisor whole numbers.
gcd_x = []
gcd_y = []

print("Find the greatest common divisor of two numbers.")
#Get user input for the two numbers.
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))

#Use for loop to find the greatest whole number divisor of the first number.
for i in range (1, x):
    check2 = x % i
    if check2 == 0:
        gcd_x.append(i)
        
#Use a second for loop to find the greatest whole number divisor of the second number.
for j in range (1, y):
    check2 = y % j
    if check2 == 0:
        gcd_y.append(j)

#Append the numbers entered to the lists.        
gcd_x.append(x)
gcd_y.append(y)

#Compare both lists of numbers.
#Start by getting the lists of each list.
list1length = len(gcd_x)
list2length = len(gcd_y)

#Nested loop that will read the index of each list and compare the values and determine the largest common divisor.
#Outer for loop that grabs the current index of the first list.
for i in range (list1length):
    current = gcd_x[i]
    #Inner for loop that grabs the index of the second list.
    for j in range (list2length):
        index = gcd_y[j]
        #Compares the index of the first list to the index of the second list.
        #If the values of each index match eachother the the values of GCD1 and GCD2 are set to that number.
        if current == index:
            GCD1 = current
            GCD2 = index

#Print results.         
print (f'The greatest common divisor of {x} and {y} is: ({GCD1}, {GCD2})')