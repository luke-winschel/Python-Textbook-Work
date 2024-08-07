#Class average: writing grades to a plain text file.  Write code that allows you to store any number of grades into a grades.txt plain text file
with open('grades.txt', mode = 'w') as grades:
    grades.write ('Smith 89 \n')
    grades.write ('Jones 73 \n')
    grades.write ('Anderson 94 \n')
    grades.write ('Williams 77 \n')
    grades.write ('Johnson 86 \n')