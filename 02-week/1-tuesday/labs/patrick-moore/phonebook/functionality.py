from data import entries
import time


def lookup_by_name(name):
    results = []
    for entry in entries:
        if name == entry['first_name']:
            results.append(entry)
        elif name == entry['last_name']:
            results.append(entry)
    return results

def add_entry():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone = input("Phone Number: ")
    entries.append({"first_name": first_name, "last_name": last_name, "phone": phone})
    print(f"{first_name} {last_name} has been added successfully!")
    return entries

#def delete_entry(name):
#    print("Name of the entry to delete: ")
#    entries.pop({"first_name": name, "last_name": last_name, "phone": phone})
#    return entries
#    print(f"{first_name} {last_name} has been deleted successfully!")
   

