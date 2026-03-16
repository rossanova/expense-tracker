from expense import Expense
from track import  Tracker
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description= "Track your expenses.")

subparsers = parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add")
add_parser.add_argument("--amount", type= float)
add_parser.add_argument("--description", type=str)

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("--id", type=int)

list_parser = subparsers.add_parser("list")

total_amount = subparsers.add_parser("summary")
total_amount.add_argument("--month", type=int)

update = subparsers.add_parser("update")
update.add_argument("--id")
update.add_argument("--field")
update.add_argument("--new_value")


args = parser.parse_args()

if args.command == "add":
    tracker = Tracker()
    tracker.load_saves()
    id = tracker.next_id()
    datenow = datetime.today()
    x = datenow.strftime("%Y-%m-%d")

    temporary_expense = Expense(
    expense_id = id,
    description = args.description,
    amount = args.amount,
    date = x
    )
    tracker.add_expense(temporary_expense)
    tracker.save_expenses()

elif args.command == "delete":
    tracker = Tracker()
    tracker.load_saves()
    tracker.delete_expense(args.id)
    tracker.save_expenses()

elif args.command == "list":
    tracker = Tracker()
    tracker.load_saves()
    print(tracker.list_expenses())

elif args.command == "summary": 
    tracker = Tracker()
    tracker.load_saves()
    if args.month == None:    
        tracker.total_amount() 
    else:
        tracker.month_total(args.month)


elif args.command == "update":
    tracker = Tracker()
    tracker.load_saves()
    new_index = int(args.id)
    new_field = str(args.field)

    tracker.update_expense(
        index_user= new_index,
        field= new_field,
        new_value= args.new_value
    )
    tracker.save_expenses()