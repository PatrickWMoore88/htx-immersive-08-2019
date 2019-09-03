#Phone Book App
#Phonebook
phonebook = {
    'A':{'Alex': '123-456-7890', 'Amy': '234-567-8901'}, 
    'B':{'Brian': '345-678-9012', 'Bobby': '456-789-0123'},
    'C':{'Chelsea': '567-890-1234', 'Candy': '678-901-2345'},
    'D':{'Derrick': '789-012-3456', 'Donnie': '890-123-4567'},
    'E':{'Erik': '901-234-5678', 'Erin': '012-345-6789'}
}
#Opening interface
print("\n========================== \n Electronic Phone Book \n========================== \n 1. Look up an entry \n 2. Set an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit")
print("==========================")
#Make your selection
selection = ""
while selection != 5:
    selection = int(input("Please select an option #: "))
#Selection Option 1: Search
    if selection == 1:
        search_name = str(input("Please input name: "))
        print("====================")
        print(f"Name: {search_name}")
        for letter in search_name[0]:
            print(f"Phone Number: {phonebook[letter][search_name]}")
            print("====================")
#Selection Option 2: Add
    elif selection == 2:
        add_name = str(input("What name would you like to add?: "))
        add_number = str(input("Please enter phone number: "))
        print("====================")
        print(f"Name: {add_name}")
        for letter in add_name[0]:
            if letter not in phonebook.keys():
                phonebook[letter]= {add_name: add_number}
            phonebook[letter][add_name] = add_number
            print(f"Phone Number: {phonebook[letter][add_name]}")
            print(f"Entry stored for {add_name}.")
        print("====================")
#Selection Option 3: Remove
    elif selection == 3:
        remove_name= str(input("What name would you like to remove?: "))
        print("====================")
        print(f"Name: {remove_name}")
        for letter in remove_name[0]:
            del phonebook[letter][remove_name] 
            print(f"Entry for {remove_name} has been removed.")
            print("====================")
#Selection Option 4: List All Entries
    elif selection == 4:
        for key, value in phonebook.items():
            print(f"{key}: ")
            print("--")
            for key, value in phonebook[key].items():
                phonebook_list = f"{str(key)}: {value}"
                print(phonebook_list)
            print("------------------")
        print("====================")
#Selection Option 5: Quit
    else:
        print("Thanks! Come back soon!")
        



