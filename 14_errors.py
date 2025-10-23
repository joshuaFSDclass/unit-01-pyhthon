"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except:
        print("num2 has to be greater than 0 !!!")
    

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
    except:
        print('The file called "r" is not found')

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
        print("look for an index that is found in the list")
    

# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)