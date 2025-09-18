'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
number = int(input("input an integer: "))
if number > 10 :
#this checks wheater or not the input is greater than 10
    print("this number is greater than ten ")
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
    #checks for the adult price 

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruit = ["bannana","pear","guinep","apple","grape","watermelon","orange","pineapple"]
fruit_input = input("what is your favorite fruit: ")
if fruit_input == fruit[0,7]:
    print("Yes, your is on the list!!!")

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
weight = float(input("what is the weight of the product: "))
if weight <= 0:
    print ("INVALID WEIGHT ERROR!!!")
else:
    #check the if the user input zero
    print("what zone are you locatde in ?")
    print(" zone opptions the: 1.zone A 2.zone B ")
    #gives the opption for the user to pick
    zone = input()
    if zone.lower() == "zone A" or zone.lower() == "a":
        shipping_cost = weight * 5
        print("shipping cost total = ",shipping_cost)
        #if zone is the a multiplay the weight of the product by five for the shipping cost 
    elif zone.lower() == "zone B" or zone.lower() == "b":
        shipping_cost = weight * 7
        print("shipping cost total = $",shipping_cost)
        #if zone is the a multiplay the weight of the product by seven for the shipping cost 
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
Side_lenght1 = int(input(" enter a side lenght:"))
Side_lenght2 = int(input(" enter a side lenght:"))
Side_lenght3 = int(input(" enter a side lenght:"))
# this is where the user would enter all of the side lengths
if  Side_lenght3 == Side_lenght2 == Side_lenght3:
    print("This is an Equilateral triangle")
    #This checks for the Equalateral triangle
elif (Side_lenght1 == Side_lenght2) or (Side_lenght3 == Side_lenght2) or (Side_lenght1 == Side_lenght3):
    print("This is an Isocseles triangle")
#checks for all possible combinationa for the Isoscelese triangle
else :
    print("This is a Scalene triangle")
#this is checks for a scalene triangle