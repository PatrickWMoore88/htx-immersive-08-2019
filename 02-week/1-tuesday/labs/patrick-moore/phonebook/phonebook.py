import functionality
import menu
import data
import view


selection = menu.menu_selection()

while selection:
    if selection == 1:
        results = functionality.lookup_by_name(input("Search by First or Last name: "))
        view.line_break()
        print("We have found the following results: ")
        view.view_entries(results)
        view.line_break()
    elif selection == 2:
        functionality.add_entry()
        view.line_break()
    elif selection == 3:
        functionality.delete_entry()
        view.line_break()
    elif selection == 4:
        functionality.show_all_entries()
    elif selection == 5:
        break
    elif selection > 5:
        print("Please try again.\nResetting...")
        view.line_break()
        selection = menu.menu_selection()
    selection = menu.menu_selection()
view.closing_banner()
