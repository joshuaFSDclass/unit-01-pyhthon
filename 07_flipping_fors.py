"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
string = "ohhhh where half way there ohhhhhh-oh living on a prayer"
for x in string:
    print(x)
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
nums = [1,2,34,6,9,5,43,]

sum = 0 

for x in nums:
    sum += x
    
print(sum)
    
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
sentence = "where does the universe come from every thing in existence."
words = sentence.split(",")
print(words)
for x in sentence:
   print(x)
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
my_dict = {
    "durian": 4,
    "mango": 1,
    "apple": 2,
}
for x in my_dict:
    print(x)