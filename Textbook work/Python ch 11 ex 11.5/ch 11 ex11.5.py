# Write a recursive function power that returns the result of a base times an exponent
sum = 1
#Get users inputs for base and expnonent
base = int(input("Please enter the base of your equation: "))
exponent = int(input("Please enter the exponent of your equation: "))

#for loop that continues to multiply the base by itself the same number of times as the exponent
for i in range (exponent):
    sum *= base
    
#Print the results
print (f"The sum of {base}^{exponent} is: ", sum)