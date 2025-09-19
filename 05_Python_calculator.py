# Welcome to the Calculatinator-inator 9000!

# Enter the first number: 10
# Enter the second number: 5

# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Floor Division
# 6. Exponential
# 7. Remainder

# Enter choice: 3

# Result: 50.0
print()
print()
print("Welcome to the Calculatinator-inator 9000!")
print()
print()
print()
num1 = float(input("Enter the first number: "))
print()
num2 = float(input("Enter the second number: "))
#user input two float values
print()
print()
print()
Opperations = int(input("Select operation" \
" 1.Adiition" \
" 2.Subtraction" \
" 3.Multiplication" \
" 4.Division" \
" 5.Floor Division" \
" 6.Exponetial" \
" 7.Remainder"
": "))
#user selects the oppereation that they want to do to numbers they input
print()
print()

if Opperations == 1:
    print(num1 + num2)
#this is the input read for addition
elif Opperations == 2:
    print(num1 - num2)
#this is the input read for subtration
elif Opperations == 3:
    print(num1 * num2)
#this is the input read for multiplication
elif Opperations == 4:
    if num2 == 0:
        print("NO dividing by zero")
    quotient = num1 / num2
    print(f"{quotient:.2f}")
#this is the input read for division but does't accept dividing by 0 with a float of two
elif Opperations == 5:
    if num2 == 0:
        print("NO dividing by zero")
    quotient = num1 // num2
    print(f"{quotient:.2f}")
#this is the input read for floor division but does't accept dividing by 0 with a float of two
elif Opperations == 6:
    product = num1 ** num2
    print(f"{product:.2f}")
#this is the input read for exponetial but does't accept dividing by 0 with a float of two
elif Opperations == 7:
    if num2 == 0:
        print("NO dividing by zero")
    print(num1 % num2)
#this is the input read for remainder but does't accept dividing by 0 with a float of two

else:
    print("ERORR")
#if user inputs any number outside the range of 1-7 what is the user would not receive an ERORR

        
