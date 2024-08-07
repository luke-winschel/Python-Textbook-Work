#(Manipulating Dates and Times with Module datetime)
from datetime import datetime

#A) Get the current date and time and store it in variable x
x = datetime.now()

#B) Repeat part (a) and store the results in variable y
y = datetime(2024, 6, 6)

#C) Display each time datetime object
print ("Date One: ",x.strftime("%c")," ", "Date Two: ",y.strftime("%c"),'\n')

#D) Display each datetime object's data attributes individually.
print ("Date One: ",x.strftime("%c"))
print ("Date Two: ",y.strftime("%c"))

#E)Use the comparison operators to compare the two datetime objects
print('\n')
#Equal/Not Equal
print ("Are the datetimes equal?")
if x == y:
    print ("The two datetime objects are the same")
else:
    print("The two datetime objects are not the same")
#Greater than and Less than
print('\n')    
print ("Which datetime object is greater than and less than")    
if x < y:
    print ("Datetime object One is less than datetime object Two")
elif x > y:
    print ("Datetime object Two is less than datetime object One")
elif x == y:
    print ("The two datetime objects are the same!")
else:
    print ("Error!")

print('\n')
#F) Calculate the difference between the two datetime objects
time_difference = x - y

print("The time difference of the two datetime objects is: ")
print (time_difference)