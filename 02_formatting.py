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
#User input a string 
if User_intput.strip() == "":
    #checks whether or not the user input any other string input other than a space
    print("invalid")
    #if conditions are met it prints "invalid"
else:
    New_user_input = User_intput.strip()
    #if conditions are not met print "valid"
    print("valid")
    print(User_intput)

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
animal = "The little ginger cat crouched low, stalking a sunbeam across the floor. This clever cat knew exactly how to find the warmest spot for an afternoon nap. Soon, the exhausted cat was dreaming about catching the elusive red dot, a truly content cat."
# A string with the word dog in it
new_animal = animal.lower().replace("cat","dog")
# replace function that replaces every uccurance of the word cat and changing it to the word dog
print(new_animal)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = input("what is your name: ")
age = input("what is your age: ")
scentence = f"your name is {name} and your age is {age}"
print(scentence)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
