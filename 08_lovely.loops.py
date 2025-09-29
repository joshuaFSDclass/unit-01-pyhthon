survey_name = input("Enter survey name: ")
#the input name of the survey
num_responses = int(input("Enter number of responses: "))
#tally the responces that the survey took
total_rating = 0
new_customers = 0

for x in range(num_responses):
    customer_type = input("Is it a returning or new customer?(type 'y' for yes type 'n' if no): ")
    # input the type of customer, new or returning 
    rating = int(input("What is the rating?(1-5): "))
    # per responce they have an inputed rating 
    total_rating += rating
    if total_rating < 1 and total_rating > 5:
        print("Invaild")
    #checks if the the user input a number not mentioned in the range
    if customer_type == "y":
        new_customers +=1
    else:
        new_customers +=0
    # tallies of new customer 
# this loop identifies the type of customer as well as the average score of all the custemers in the survey
avg_rating =total_rating/num_responses
print(f"the average rating in the survey = {avg_rating}")

print(new_customers)
#prints the average rating and the amout of new customers.