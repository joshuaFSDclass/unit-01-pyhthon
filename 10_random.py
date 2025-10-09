
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
from random import randint
# imports the random integer moduel
for x in range(10):
    roll_dice = randint(1, 6)
    print(roll_dice)
#prints a randome number from
    
"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
from random import uniform, random
for x in range(5):
    randDec = random()
    print(randDec)
for x in range(5):
    randDec1 = uniform(10.0, 20.0)
    print(randDec1)

"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
from random import choice
colors = ["red","blue","green","yellow","purple"]
for v in range(3):
    print(choice(colors))


"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
from random import shuffle
for z in numlist:
    shuffle(numlist)
    print()
    print(numlist)