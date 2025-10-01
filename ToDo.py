with open("Todos.txt") as file:
    my_todo_list = file.readlines()
while True:
    add_or_remove = input("would you like to add the an item: type 'y' for yes or 'n' for no would you like to exit then type 'e': ")
    #the user chooses to create add to the todo list
    print()
    for x in my_todo_list:
        print(x)
        #print all of the items in the list of the
    if  add_or_remove == "y":
        #if they choose the yes the add a task to the list
        print()
        print()
        userInput = input("write a tasks: ")
        #user inputs the task
        print()
        print()
        my_todo_list.append(userInput)
         
    elif add_or_remove == "n":
        #if the user chooses no the get to remove a item from the list
        choice = int(input("which number item would you like to remove: "))
        print()
        print()
        print()
        del my_todo_list[choice - 1]
        #user chooses the number of the item in the list to remove
    elif add_or_remove == "e":
        with open("Todos.txt") as file:
            my_todos_list = file.writelines()
            
    else:
        print("invalid")
    

        

