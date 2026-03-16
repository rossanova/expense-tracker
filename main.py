from expense import Expenses
from track import  Tracker
import json
import datetime
import argparse


track = Tracker()

while True:
    print("1 - Add an Expense")
    print("2 - Update an Expanse")
    print("3 - Delete an Expense")
    print("4 - View all Expenses")

    x = input("Enter your input: ")

    if x == "1":
        r = Expenses()
        r.create_expense(
            name = input("Create a name: "),
            value = float(input(f"Create a value: ")),
            date = (input("Create a date: ")),
        )
        track.add_expense(r)

    elif x == "2":
        if len(track.list) == 0:
            print("There are no expenses to be actualized")
        else:
            print(track)

            try:
                index_user = int(input("Which expense do you want to change? "))
            except ValueError, IndexError, TypeError, NameError:
                print("Please enter a valid index")
            else:
                field = input("What field a change: ")
                new_value = input("Insert the new value: ")   
                track.update_expense(index_user, field, new_value )

    elif x == "3":
        if len(track.list) == 0:
            print("There is no expenses to be deleted")
        else:
            print(track)
            z = int(input("Which expense do you want to delete? "))
            track.delete_expense(z)

    elif x == "4":
        print(track)
    else:
        break
    