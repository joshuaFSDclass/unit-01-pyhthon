"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""
# The function will have divide by zero error
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except:
        print("num2 has to be greater than 0 !!!")
# When the devide by zero error comes up print this message to user
    

# Example usage:
divide_numbers(10, 0)

"""
Example 2: Opening Files
"""

def read_file(filename):
    try:
        file = open(filename, 'r')
        contents = file.read()
        print("File contents:", contents)
        file.close()
        # The code segment is reading an file that does not exsist 
    except:
        print('The file called "r" is not found')
        # when a nonexisting file is thier the code will continue with this message printed

# Example usage:
read_file("nonexistent.txt")

"""
Example 3: List Items
"""

def get_item(lst, index):
    try:
        item = lst[index]
        print("Item:", item)
    except:
        print("index is out of range")
        # when the index that is beeing returned s higher than the max index of the list print this message.
    

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)
# the get_item(my_list,5) is out of the range of the list

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value:", value)
    except:
        print("This key does not exist")
#if the fucntion is missing the key that is beeing called then the prgram will print this message and continue
# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")
# the c key is not found in the dictionary function 
"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
        # when the file is not found this message will print and the prgram will continue
    else:
        print("File located")
        # when the file is licated and the and no error occors the program will comence and print this message


# Example usage:
process_file("example.txt")