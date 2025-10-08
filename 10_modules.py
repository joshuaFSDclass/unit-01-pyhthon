import os
import sys
"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
workingDirectory = os.getcwd
print(workingDirectory)
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
test_folder = os

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""
drct = "data"
if os.path.isdir(drct):
    print("Directory already exists.")
else:
    os.makedirs(drct)
    print(f"Directory {drct} created.")
"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
drct2 = "config.txt"
if os.path.isfile(drct2):
    print("myPythonfiles/config.txt")
else:
    print("File not found.")

"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print(sys.version)
print(sys.version_info)

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
# Get the platform string
platform = sys.platform

# Map the platform string to user-friendly names
if platform.startswith('linux'):
    friendly_name = 'Linux'
elif platform == 'win32':
    friendly_name = 'Windows'
elif platform == 'darwin':
    friendly_name = 'MacOS'
else:
    friendly_name = f'Unknown platform: {platform}'

# Print the result
print(f"You are running on: {friendly_name}")
