contactbook = {

}
# the dictionary fom which the contact list is formed 
while True:
   
    print("Contact Book Menue:" \
    "1. Add Contact" \
    "2. Delete Contact" \
    "3. List contacts" \
    "4. Exit")
    #presents the opption for the contact list program
    print()
    choice = int(input("Enter your choice: "))
    print()
    if choice == 1:
        name = input("what is the contact name? : ")
        #user inputs the name of contact 
        print()
        num = int(input("what is their number? : "))
        print()
        contactbook[name] = num
    if choice == 2:
        name = input("what is the contact name? : ")
        del contactbook[name]
        print()
    if choice == 3:
        for x in contactbook:
            print(x, contactbook[x])
            print()
    if choice == 4:
        break


