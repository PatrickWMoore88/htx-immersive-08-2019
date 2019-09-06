def show_menu():
    print("========================== \n Electronic Phone Book \n========================== \n 1. Look up an entry \n 2. Add an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit")
    print("==========================")

def prompt_user():
    return int(input("Please select a #: "))

def menu_selection():
    show_menu()
    return prompt_user()

