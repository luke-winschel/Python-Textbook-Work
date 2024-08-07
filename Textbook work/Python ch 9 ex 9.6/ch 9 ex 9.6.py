#Class Average: writing a gradebook dictionary to a JSON file.  Write code that creates a JSON dictionary that allows an instructor to input a students first and last name, and exam 1,2, and 3 scores.
import json


students = [
   {'first_name': 'John', 'last_name': 'Smith', 'exam1': 85, 'exam2': 90, 'exam3': 92},

   {'first_name': 'Ashley', 'last_name': 'Martin', 'exam1': 92, 'exam2': 88, 'exam3': 95},

   {'first_name': 'Andrea', 'last_name': 'Johnson', 'exam1': 78, 'exam2': 85, 'exam3': 80},

   {'first_name': 'Steve', 'last_name': 'Anderson', 'exam1': 90, 'exam2': 92, 'exam3': 94},

   {'first_name': 'Mike', 'last_name': 'Smith', 'exam1': 88, 'exam2': 90, 'exam3': 85}
]

gradebook_dict = {'students': students}

with open('grades.json', 'w') as f:

   json.dump(gradebook_dict, f)

