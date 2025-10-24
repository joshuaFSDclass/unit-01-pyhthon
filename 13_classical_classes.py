"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
    # the class that defines the atributes of a person
    def __init__(self, name, age):
    # leave the name and the age to be defined later
        self.name = name 
        self.age = age 
    def hi(self):
        print("Hi my name is " + self.name)
    # An itroduction from the specific person

Joshua = Person("Joshua", 18)
#defines the objects in the person class
print(Joshua.name)
print(Joshua.age)
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animals:
   def speak(self):
        print("the animal speaks")
#parent class defines animals speaking
class Dog(Animals):
    def speak(self):
        print("Bark")
# defines how a dog would speak according        
dog = Dog()
dog.speak()

class Cat(Animals):
    def speak(self):
        print("Meow")
# defines how a cat would speak according
cat = Cat()
cat.speak()
#

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
class BankAccount:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner
        # Adds to the value of your account
    def deposit(self, amount):  
        if amount > 0:
            self.balance += amount
        print(f"Successfullt depostitied ${amount}. Your new balance is ${self.balance}")
    # Subtracts how much you would like to withdraw from your balance
    def withdraw(self, amount_2):
        if amount_2 < 0:
            self.balance -= amount_2
            print(f"Successfully withdrew ${amount_2}. Your new balance is ${self.balance}")
