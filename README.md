# Tutedude_python_assignment3
Task 1: Calculate Factorial Using a Function 

Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

-Program:
-2 functions are created
-1. def factorial_rec : it will calculate factorial using recursion
-if number is 1, then it will return 1, since factorial of 1 is 1
-else
-factorial is return as num*factorial_rec(num-1) <-- this factorial_rec(num-1) will goes on until it reach factorial(1), which is equal to 1 and then the factorial will be calculated backwards.

-2nd: def factorial_loop : it will calculate factorial using loop
-factorial is stored in fact, initial value stored is 1
-while loop will run until the number becomes 1
-  fact = fact*num
-  num= num-1
-return fact
-user will input the number, done by using input()
-print the factorial by calling both functions.


Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)

-Code:
-Import math will import all the math modules.
-user will input the number, done by using input()
-if number is not digit, it will print error, if valid digit, the program will continue

-square root is calculated using math.sqrt(num)
-logarithm is calculated using math.log(num)
-sine is calculated using math.sin(num)

