Example problems are from Introduction to Python for Computer Science and Data Science.  Learning to Program with AI, Big Data, and the Cloud.  By Paul Deitel and Harvey Deitel.

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 1:  Introduction to Computers and Python

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 2:  Introduction to Python Programming.

  * Exercise 2.6: (Odd or Even)  Use if statements to determine whether an integer is odd or even.  [Hint: Use the remainder operator.  An even       number is a multiple of 2.  Any multiple of 2 leaves a remainder of 0 when divided by 2.]

  * Exercise 2.8:  (Table of Squares and Cubes)  Write a script that calculates the squares and cubes of the numbers from 0 to 5.  Print the          resulting values in table format, as shown below.  Use the tab escape sequence to achieve the three-column output.

  * Exercise 2.10 (Arithmetic, Smallest to Largest)  Write a script that inputs three integers from the user.  Display the sum, average, product,     smallest, and largest of the numbers.  Note that each of these is a reduction in functional-style programming.

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 3: Control Statements and Program Development

  * Exercise 3.13: (Factorials)  Factorial calculations are common in probability.  The factorial of a nonnegative integer n is written as n!         (pronounced  "n factorial") and is defined as follows:
    
      n! = n * (n - 1) * (n - 2) * ... * 1
    
    for values of n greater than or equal to 1 with 0! defined to be 1, so:
    
      5! = 5 * 4 * 3 * 2 * 1
    
    which is 120.  Factorials increase in size very rapidly.  Write a script that inputs a nonnegative integer and computes and displays its          factorial.

  * Exercise 3.16: (Nested Control Statements)  Use loops to find the two largest values of 10 numbers entered.

  * Exercise 3.21: (Calculate Change Using fewest Number of Coins)  Write a script that inputs a purchase price of a dollar or less for an item,      Assume the purchaser pays with a dollar bill.  Determine the amount of change the cashier should give back to the purchaser.  Display the         change using the fewest number of pennies, nickels, dimes, and quarters.

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 4:  Functions
  
  * Exercise 4.9:  (Temperature Conversion)  Implement a Fahrenheit function that returns the Fahrenheit equivalent of a Celsius temperature.         Use the following formula:
    
       F = (9 / 5) * C + 32

    Use this function to print a chart showing the Fahrenheit equivalents of all Celsius temperatures in the range of 0-100 degrees.  Use one         digit of precision for the results.  Print the outputs in neat tabular format.

  * Exercise 4.10:  (Guess the Number)  Write a script that plays "Guess the number."  Choose the number to be guessed by selecting a random          integer in the range 1 to 20.  Do not reveal the number to the user. The player inputs a first guess.  If     the guess is incorrect display      "Too High", or "Too Low" as appropriate to help the player "zero in" on the correct answer, display "Congratulations.  You guessed the            number!", and allow the user to choose whether to play again.

  * Exercise 4.14:  (Computer-Assisted Instruction)  Computer-assisted instruction (CAI) refers to the use of computers in education.  Write a        script to help an elementary school student learn multiplication.  Create a function that randomly generates and returns a tuple of two           positive integers.  Use that function's result in your script to prompt the user to find the sum of the two generated integers.  For a            correct answer, display the message "Very Good!" and ask another multiplication question.  For an incorrect answer, display the message "No.      Please try again!" and let the student try the same question repeatedly until the student finally gets it right.
    
--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 5:  Sequences: Lists and Tuples.

  * Exercise 5.6:  (Function Returning Tuples)  Define a function rotate that receives three arguments and returns a tuple in which the first         argument is at index 1, the second argument is at index 2 and the third argument is at index 0.  Define variables a, b, and c containing          'Doug', 22, and 1984.  Then call the function three times.  For each call, unpack its results into a, b, and c, then display their values.
    
  * Exercise 5.7:  (Duplicate Elimination)  Create a function that receives a list and returns a (possibly shorter) list containing only the          unique values in sorted order.  Test your function with a list of numbers and a list of strings.

  * Exercise 5.20:  (Display a Two-Dimensional list in Tabular Format)  Define a function named display_table that receives a two-dimensional         list and displays its contents in tabular format.  List the column indices as headings across the top and list the row indices at the left of     each row.

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 6: Dictionaries and Sets.

  * Exercise 6.5:  (Counting Duplicate Words)  Write a script that uses a dictionary to determine and print the number of duplicate words in a        sentence.  Treat uppercase and lowercase letters the same and assume there is no punctuation in the sentence.  Use the techniques you learned     in Section 6.2.7.  Words with counts larger than 1 have duplicates.

  * Exercise 6.10: (Set Manioulations) Use the following sets:
       {'red', 'green' 'blue}
       {'cyan', 'green', 'blue', 'magenta', 'red'}
    
    Display the results of:
        a) comparing the sets using each of the comparison operators.
        b) combining the sets using each of the mathematical set operators.
    
   * Exercise 6.13: (Synonyms Dictionary) Use an online thesaurus to look up synonyms for five words, then create a synonyms dictionary that maps      those words to lists containing three synonyms for each word.  Display the dictionary's contents as a key with an indented list of synonyms       below it.

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 7: Array-Oriented Programming with NumPy.

   * Exercise 7.3: (Element-Wise Array Multiplication) Create a 3-by-3 array containing the even integers from 2 through 18.  Create a second          3-by-3 array containing integers from 9 down to 1, then multiply the first array by the second array.

   * Exercise 7.18: (Median and Mode of an Array) NumPy arrays offer a mean method, but not median or mode.  Write functions median and mode that      use existing NumPy capabilities to determine the median (middle) and mode (most frequent) of the values in an array.  Your functions should       determine the median and mode regardless of the array's shape.  Test your function on three arrays of different shapes

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 8: Strings: A Deeper Look

   * Exercise 8.7: (Converting Integers to Characters) Use the c presentation type to display a table of the character codes in the range 0 to         255 and their corresponding characters.

   * Exercise 8.18: (Regular Expression: Password Format Validator) Search online for secure password recommendations, then research existing           regular expressions that validate secure passwords.  Two examples of a password requirement are:

        * Passwords must contain at least five words, each separated by a hyphen, a space, a period, or an underscore.
    
        * Passwords must have a minimum of 8 characters and contain at least one each from uppercase characters, lowercase characters, digits,              and punctuation characters (such as characters in '!@#$%^&*?').

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 9: Files and Exceptions.

   * Exercise 9.1: (Class Average: Writing Grades to a plain text file)  Figure 3.2 presented a class average script in which you could enter any       number of grades followed by a sentinel value, and then calculate the class average.  Another approach would be to read grades from a file.
     In an IPython session, write code that enables you to store any number of grades into a grades.txt plain text file.
     
   * Exercise 9.2: (Class Average: Reading Grades from a Plain Text File) In an IPython session, write code that reads the grades from the              grades.txt file you created in the previous exercise.  Display the individual grades and their total, count, and average.

   * Exercise 9.3: (Class average: Writing Student Records to a CSV file) An instructor teaches a class in which each student takes three exams.       The instructor would like to store this information in a file named grades.csv for later use.  Write code that enables an instructor to           enter each student's first name and last name as strings and the student's three exam grades as integers. Use the csv module to write each        record into the grades.csv file.  Each record should be a single line of text in the following CSV format:
         firstname, lastname, exam1grade, exam2grade, exam3grade.

   * Exercise 9.6: (Class Average: Writing a Gradebook Dictionary to a JSON File) Reimplement Exercise 9.4 using the JSON module to write the          student information to the file in JSON format.  For this exercise, create a dictionary of student data in the following format:
     
        gradebook_dict = {'students': [student1dictionary, student2dictionary, ...]}

     Each dictionary in the list represents one student and contains the keys 'first_name', 'last_name', 'exam1', 'exam2', and 'exam3', which map      to the values representing each student's first name (string), last name (string), and three exam scores (integers).  Output the                  gradebook_dict in JSON format to the files grades.json.

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 10: Object-Oriented Programming.

   * Exercise 10.3: (Time Class Enhancement) Modify Section 10.4.2's Time class to provide a read-only property universal_str that returns a           string representation of a Time in 24-hour clock format with two digits each for the hour, minute, and second, as in '22:30:00' (for 10:30        PM) or '06:30:00' (for 6:30 AM).  Test your new read-only property

   * Exercise 10.7: (Manipulating Dates and Times with Module datetime) The Python Standard Library's datetime module contains a datetime class        for manipulating dates and times.  The class provides various overload operators.  Research class datetime's capabilities, then perform the       following tasks:
         a) Get the current date and time and store it in variable x.
         b) Repeat Part (a) and store the results in variable y.
         c) Display each datetime object.
         d) Display each datetime object's data attributes individually.
         e) Use the comparison operators to compare the two datetime objects.
         f) Calculate the difference between y and x.

   * Exercise 10.10: (Invoice Class) Create a class called Invoice that a hardware store might use to represent an invoice for an item sold at         the store.  An Invoice should include four pieces of information as a data attributes - a part number (a string), a part description (a           string), a quantity of the item being purchased (an int), and a price per item (a Decimal).  Your class should have an __int__ method that        initializes the four data attributes.  Provide a property for each data attribute.  The quantity and price per item should be non-negative        - use validation in the properties for these data attributes to ensure that they remain valid.  Provide calculate_invoice method that             returns the invoice amount (that is, multiplies the quantity by the price per item). Demonstrate class Invoice's capabilities.

--------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 11: Computer Science Thinking: Recursion, Searching, Sorting, and Big O.

   * Exercise 11.5: (Recursive power Function) Write a recursive function power(base, exponent) that, when called, returns:

        base^exponent

     For Example, power (3,4) = 3 * 3 * 3 * 3.  Assume that exponent is an integer greater than or equal to one.  Hint: The recursion step should      also use the relationship:
     
        base^exponent = base * base^(exponent - 1)

     and the terminating condition occurs when exponent is equal to 1 because:

        base^1 = base

     Incorporate this function into a program that enables the user to enter the base and exponent.

   * Exercise 11.9: (Greatest Common Divisor) The greatest common divisor of integers x and y is the largest integer that evenly divides into          both x and y.  Write and test a recursive function gcd that returns the greatest common divisor of x and y.  The gcd of x and y is defined        recursively as follows: If y is equal to 0, then gcd (x,y) is x; otherwise, gcd (x,y) is gcd (y, x % y) where % is the remainder operator. 
