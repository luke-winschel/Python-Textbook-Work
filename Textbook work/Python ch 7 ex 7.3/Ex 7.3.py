#(Element-Wise Array Multiplication) Create a 3x3 array with even intergers between 2-18 and another 3x3 array with numbers 9-1.  Multiply the two arrays

#Import numpy library
import numpy as np

#Set parameters for first array
#Finds all even numbers between 2-20
a = np.array([x for x in range (2,20,2)])

#Set parametes for second array
#Finds all numbers between 9-0 counting down from 9
b = np.array([x for x in range (9, 0, -1)])

#Third array stores the values of the two arrays multiplied
c = np.array(a * b)

#Print all three arrays and formats them in a 3x3 array.
print ("Array 1: \n",a.reshape(3,3),"\n")
print ("Array 2: \n",b.reshape(3,3),"\n")
print ("Multipled: \n", c.reshape(3,3),"\n")
