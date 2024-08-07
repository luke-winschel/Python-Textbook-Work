#Class average: reading grades from a plain text file.  Write code that reads the grades from the grades.txt file
with open('grades.txt', mode ="r") as grades:
    print (f'{"Name":<10}{"Grade": >10}')
    for record in grades:
        name, grade = record.split()
        print(f'{name:<10}{grade:>10}')