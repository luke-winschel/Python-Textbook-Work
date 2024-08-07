#Class average: Writing student records to a CSV file. Write code that enables an instructor to enter each students first and last name as strings and the 3 exam grades as integers.
import csv

num_students = int(input("How many students do you have: "))

with open('grades.csv', mode = 'w', newline = '') as grades:

    for i in range(num_students):
        first_name = str(input("Please enter the students first name: "))
        last_name = str(input("Please enter the students last name: "))
        exam1grade = int(input("Please enter the grade for the first exam: "))
        exam2grade = int(input("Please enter the grade for the second exam: "))
        exam3grade = int(input("Please enter the grade for the third exam: "))
        print("\n")
        
        for a in range (1):
            writer = csv.writer(grades)
            writer.writerow([first_name, last_name, exam1grade, exam2grade, exam3grade])