#Factorial of a function using recursion and loop

def factorial_rec(num1):
    if num1==1:
        return 1
    else:
        return num1*factorial_rec(num1-1)

def factorial_loop(num2):
    fact=1
    while num2!=1:
         fact *= num2
         num2-=1
    return fact

num = int(input("Enter a number:"))
print (f"Factorial of {num} is: {factorial_rec(num)}")
print (f"Factorial of {num} is: {factorial_loop(num)}")