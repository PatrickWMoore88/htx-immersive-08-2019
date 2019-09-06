import time


def view_entries(entries):
    number_of_entries = len(entries)
    if number_of_entries:
        print(f"Entries Found: {number_of_entries}")
        for entry in entries:
            print(f"{entry['first_name']} {entry['last_name']} {entry['phone']}")
    else:
        print("There are no entries found. Please try again.")

def line_break():
    print("====================")
    time.sleep(4)

def closing_banner():
    print("*" + ("-" * 30) + "*")
    print("| " + "Thank you!! Come back soon!!" + " |")
    print("*" + ("-" * 30) + "*")