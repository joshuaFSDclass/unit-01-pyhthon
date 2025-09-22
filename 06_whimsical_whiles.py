"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 1 
while i < 11:
#itarates when "i" value is less than 11
    print(i)
    i += 1
#adds the 1 to "i"
# counts to 10 
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
while i > 0 :
#itarates when "i" is greater than 0
    i -= 1
    print(i)
#subtracts 1 from "i" 
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
num1 = int(input("enter a number: "))
#user input
t = 1
while num1 > 0:
#iterates when input is greater than 0 
    t = num1 * t
#multiplies the input by itself 
    num1 -= 1
# assigns new in put to varriable
print(t)
#prints the product of the old input and the "t" value
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
x = 1
username = input ("Enter Username: ")
password = input("Enter your Password: ")
while password != "chimychangah" and x < 10:
    x += 1 
    print("Error incorecet password!!!")
    password = input("Enter your Password: ")
    print(x, "Attemps")
else:
    print("hi",username)
   
"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""