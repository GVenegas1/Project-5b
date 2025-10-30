# project-5b

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 10/29/2025
# Description: Using a function called add_surname that takes a list
# of first names and returns a new list of names.

def add_surname(names):
    """Returns a new list containing only the names that start
        with 'K' and followed by the surname 'Kardashian'"""

    #A list to filter, modify names, and check for empty strings
    return [name + " Kardashian" for name in names if len(name) > 0 and name[0] == "K"]

#example used
#first_names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
#result = add_surname(first_names)
#print(result)