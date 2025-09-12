"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
Password_input = input("enter the password: ")
if Password_input.lower() == "letmein":
    #changed made the input change to lower case evry time it was enterd
    print("Welcome user")
else:
    print("Wrong password")

    

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
User_intput = input("input any string of your choice: " )
if User_intput.strip() == "":
    print("invalid")
else:
    New_user_input = User_intput.strip()
    print("valid")
    print(User_intput)

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""