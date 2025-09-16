'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
number = int(input("input an integer: "))
if not(number < 10 and number % 2 == 0):
#this checks wheater or not the input is greater than 10 and even
    print("this number is greater than ten and even")
# prints this message if condition is met
else:
    print("Flase")
#print if conditions are not met
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
ticket_price = int(input("Type the your ticket price: $"))
if ticket_price == 10:
    print("This is a minors ticket.")
# checks is the input
if ticket_price == 20:
    print("This is an adult ticket.")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''


'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''