Example problems are from Introduction to Python for Computer Science and Data Science.  Learning to Program with AI, Big Data, and the Cloud.  By Paul Deitel and Harvey Deitel.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 1:  Introduction to Computers and Python

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 2:  Introduction to Python Programming.

  * Exercise 2.6: (Odd or Even)  Use if statements to determine whether an integer is odd or even.  [Hint: Use the remainder operator.  An even number is a multiple of 2.  Any multiple of 2 leaves a remainder of 0 when divided by 2.]

  * Exercise 2.8:  (Table of Squares and Cubes)  Write a script that calculates the squares and cubes of the numbers from 0 to 5.  Print the resulting values in table format, as shown below.  Use the tab escape sequence to achieve the three-          column output.

  * Exercise 2.10 (Arithmetic, Smallest to Largest)  Write a script that inputs three integers from the user.  Display the sum, average, product, smallest, and largest of the numbers.  Note that each of these is a reduction in functional-style        programming.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 3: Control Statements and Program Development

  * Exercise 3.13: (Factorials)  Factorial calculations are common in probability.  The factorial of a nonnegative integer n is written as n! (pronounced  "n factorial") and is defined as follows:
      n! = n * (n - 1) * (n - 2) * ... * 1
    for values of n greater than or equal to 1 with 0! defined to be 1, so:
      5! = 5 * 4 * 3 * 2 * 1
    which is 120.  Factorials increase in size very rapidly.  Write a script that inputs a nonnegative integer and computes and displays its factorial.

  * Exercise 3.16: (Nested Control Statements)  Use loops to find the two largest values of 10 numbers entered.

  * Exercise 3.21: (Calculate Change Using fewest Number of Coins)  Write a script that inputs a purchase price of a dollar or less for an item,  Assume the purchaser pays with a dollar bill.  Determine the amount of change the cashier should         give back to the purchaser.  Display the change using the fewest number of pennies, nickels, dimes, and quarters.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 4:  Functions
  
  * Exercise 4.9:  (Temperature Conversion)  Implement a Fahrenheit function that returns the Fahrenheit equivalent of a Celsius temperature.  Use the following formula:
      F = (9 / 5) * C + 32
    Use this function to print a chart showing the Fahrenheit equivalents of all Celsius temperatures in the range 0-100 degrees.  Use one digit of precision for the results.  Print the outputs in neat tabular format.

  * Exercise 4.10:  (Guess the Number)  Write a script that plays "guess the number."  Choose the number to be guessed by selecting a random integer in the range 1 to 20.  Do not reveal the number to the user. The player inputs a first guess.  If     the guess is incorrect display "Too High", "Too Low" as appropriate to help the player "zero in" on the correct answer, display "Congratulations.  You guessed the number!", and allow the user to choose whether to play again.

  * Exercise 4.14:  (Computer-Assisted Instruction)  Computer-assisted instruction (CAI) refers to the use of computers in education.  Write a script to help an elementary school student learn multiplication.  Create a function that randomly          generates and returns a tuple of two positive integers.  Use that function's result in your script to prompt the user to find the sum of the two generated integers.  For a correct answer, display the message "Very Good!" and ask another           multiplication question.  For an incorrect answer, display the message "No.  Please try again!" and let the student try the same question repeatedly until the student finally gets it right.
    
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 5:  Sequences: Lists and Tuples.

  * Exercise 5.6:  (Function Returning Tuples)  Define a function rotate that receives three arguments and returns a tuple in which the first argument is at index 1, the second argument is at index 2 and the third argument is at index 0.  Define      variables a, b, and c containing 'Doug', 22, and 1984.  Then call the function three times.  For each call, unpack its results into a, b, and c, then display their values.
    
  * Exercise 5.7:  (Duplicate Elimination)  Create a function that receives a list and returns a (possibly shorter) list containing only the unique values in sorted order.  Test your function with a list of numbers and a list of strings.

  * Exercise 5.20:  (Display a Two-Dimensional list in Tabular Format)  Define a function named display_table that receives a two-dimensional list and displays its contents in tabular format.  List the column indices as headings across the top        and list the row indices at the left of each row.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chapter 6: Dictionaries and Sets.

  * Exercise 6.5:  (Counting Duplicate Words)  Write a script that uses a dictionary to determine and print the number of duplicate words in a sentence.  Treat uppercase and lowercase letters the same and assume there is no punctuation in the         sentence.  Use the techniques you learned in Section 6.2.7.  Words with counts larger than 1 have duplicates.

  * Exercise 6.10:
