#Exercise 4.9
"""(Temperature conversion) Implement a Fahrenheit function that returns the Fahrenheit equivalent of a Celsius temperature. Use this function to print a chart of Fahrenheit temperatures to Celsius"""

number = 0

#Define function that converts Celsius to Fahrenheit
def conversion(number):
    farenheit = (9/5) * number + 32

    return farenheit


#Create loop that calculates the Fahrenheit equivilents of Celsius temps
for i in range (100):
    #prints Celsius and Fahrenheit value on the same line
    print (f'{i:2} C | {conversion(i):.2f} F' )
