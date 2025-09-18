print("Room opptions: 1.study Room 2.computer lab 3.reading conner")
area =input("Which library area :")
#takes input on the area in the library.
noise =int(input ("what is the noise level on a scal of 1-10"))
#checks input on the nois level.
print("Example of times: 1.Morning 2.lunch 3.afternoon")
Time_of_day = input("what time of day is this is it :")
#takes input on the time of day.
num_of_people = int(input("how many people are in the library: "))
#takes the input on the number of students.


study_room = 4
computer_lab = 6
reading_conner = 2
 #limit for noise level in each section of library
if Time_of_day == "lunch":
   study_room += 2 
   computer_lab += 2
   reading_conner += 2
   # check if the user inputs lunch then if so adds 2
if num_of_people > 10:
    study_room += 1
    computer_lab += 1
    reading_conner += 1
    #checks if the user inputs lunch then if so adds 1

if noise > study_room:
    print("fail")
else:
    print("pass")
    #passes or fails the if person nios level is below threshold
     
if noise > computer_lab:
    print("fail")
else:
    print("pass")
    #passes or fails the if person nios level is below threshold

if noise > reading_conner:
    print("fail")
else:
    print("pass")
    #passes or fails the if person nios level is below threshold
     
       

    
    