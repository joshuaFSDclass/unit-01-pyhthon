"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
number_float = 30.89
print(number_float)
number_int = int(number_float)
print(number_int)
# I turned 30.0 into the integer 30
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
positive_Or_negative = int(input("number"))
if positive_Or_negative > 0 :print("this number is positive")
# takes a number input checks if it's greater than zero, then prinst that it is positive 
elif positive_Or_negative < 0 :print("this number is negative")
# takes a number input checks if it's ldss than zero, then prints that it is negative
elif positive_Or_negative == 0 : print("this number is zreo")
 # determines that the input is 0 then prints that it is Zero

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
floating_number = float(input("enter a desimal point "))
# made a user input to type in a floating point value
i_nteger = int(input("enter a whole number "))
# made a user input to type in an integer value
sum1 = floating_number + i_nteger 
sum2 = floating_number - i_nteger
# created a "sum" varriable and added i_nteger to floating_number and the subtracted 2
product = floating_number * i_nteger 
#created a "product" varriable to multiply the "sum" value by 13
quotient = floating_number / i_nteger
# made "quatient" that divides the "product" value by 2
print("quotients ", quotient)
print("product ",product)
print("the first Sum: ",sum1)
print(" the second Sum: ",sum2)
# printed the value of "quotient"


"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
fruit =  {
                'bannana':27,
                'coconut':10
            }
# ditionary holding the number of fruit in the store 
print("there are", fruit["bannana"],"Bannanas in the store")
# printing the number of bannanas in the store
print("there are", fruit["coconut"],"Coconuts in the store")
# printing the nuber of coconuts in the store 
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
my_list = "1,2,3,4,5"
tuple(my_list)
# turned the my_list into the a tuple. 
print(my_list)
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
Subjects = ["Algebra","Fullstack development","Advanced orchestra","Statistics"]
#list of the subject that i like throughout highschool
my_string = "-".join (Subjects)
# i joint the bujects with a dash 
print(my_string)
print(Subjects)
