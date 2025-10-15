"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
from datetime import date, datetime
#allso datetime was imported in datetime 
#impports the date time module and uses the dat class to pull the current date  
DATE = date.today()
print(DATE)
#prints current date

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
eDate = datetime.now()

string = eDate.strftime('%m/%d/%Y')
print (string)
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
newstring = "07,22,2000"
my_date = datetime.strptime(newstring, "%m/%d/%Y")
print(my_date)
"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
print()
print()
birth = input("When is your birthday? (m/d/Y)")
birthed = datetime.strptime(birth, "%m/%d/%Y")
birthed2 = datetime.now() - birthed
birthed3 = birthed2.days//365
print("you are", birthed, "year old")