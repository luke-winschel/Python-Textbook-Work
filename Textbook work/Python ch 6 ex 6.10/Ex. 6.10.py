#Exercise 6.10
#(Set manipulation) Using the following sets: {'red', 'green', 'blue'}  and {'cyan', 'green', 'blue', 'magenta', 'red'} display the following: Comparing the sets using comparison operators and combine the sets using mathmatical operators

#Part A: Comparing the sets using the each of the comparison operators
print('\t' '\t' '\t' 'Comparison operators')

print('\n')

#if sets match
print("{'red', 'green', 'blue'} == {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} == {'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#If sets do not match
print("{'red', 'green', 'blue'} != {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} != {'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#If set one is greater than or equal to second set
print("{'red', 'green', 'blue'} >= {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} >= {'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#If set one is less than or equal to second set
print("{'red', 'green', 'blue'} <= {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} <= {'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#Checks for improper subset
print("{'red', 'green', 'blue'}.issubset {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'}.issubset({'cyan', 'green', 'blue', 'magenta', 'red'}))

print('\n')

#Checks for improper supersets
print("{'red', 'green', 'blue'}.issuperset {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'}.issuperset({'cyan', 'green', 'blue', 'magenta', 'red'}))


print ('\n')
#Part B: combining the sets of each of the Mathematical set operators
print('\t' '\t' '\t' 'Mathematical Operators')

print('\n')

#Combines the two sets into a single set
print("{'red', 'green', 'blue'} | or .union {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} | {'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#Finds elements where the sets match
print("{'red', 'green', 'blue'} & or .intersection {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} & {'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#Finds differences between the two sets
print("{'red', 'green', 'blue'} - or .difference {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} -{'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#Finds the symmetric differences
print("{'red', 'green', 'blue'} ^ or .symmetric_difference {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'} ^ {'cyan', 'green', 'blue', 'magenta', 'red'})

print('\n')

#Determines if the two sets do not have any common elements
print("{'red', 'green', 'blue'} .isdisjoint {'cyan', 'green', 'blue', 'magenta', 'red'}")
print({'red', 'green', 'blue'}.isdisjoint({'cyan', 'green', 'blue', 'magenta', 'red'}))