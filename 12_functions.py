"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
def greeting(name):
    """
    This function greets the inputed name
    """
    print("hello" + name)
greeting(" josh")
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def square(a):
    """
    this function multiplies the inputed number by its self

    formula:
    (a * a) or (a ^ 2)
    """
    return a ** 2
square(3)

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
def evenOdd(a):
    """
    this function determines wheather or not a number is even 

    if the moduler of the number is equal to 0 the number  is even and if it's greater than zero its odd
    """
    if a % 2 == 0:
        return True
    else:
        return False
y = evenOdd(3)
print(y)

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def area(l, w):
    """
    this fuction multilplies the both side lenghts inputed and give the area

    formula:
    length X width
    """
    return l * w


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def tempconvert(H):
    """
    this function convert celsius to fahrenheit

    formula:

    temperature x 2 + 30 

    """
    return (H * 2) + 30

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
def avg(numbers):
    """
    this function decribes the average of the lisy of numbers

    formula:
    
    Sum of numbers in the list divided by the number of elemenst in th list 
    """


    return sum(numbers) / len(numbers)
x = avg([1,2,3,4,5,6,7,8,9,10,])
print(x)
"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""