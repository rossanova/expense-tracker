from expense import Expense
from track import  Tracker
import argparse
import datetime

parser = argparse.ArgumentParser(description= "Track your expenses.")

subparsers = parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add")
add_parser.add_argument("--amount", type= float)
add_parser.add_argument("--description", type=str)

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("--id", type=int)

list_parser = subparsers.add_parser("list")

total_amount = subparsers.add_parser("summary")

month_total = subparsers.add_parser("summary-monthly")
month_total.add_argument("--month", type=int)

update = subparsers.add_parser("update")
update.add_argument("--index")
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
    print(tracker)

elif args.command == "summary": 
    tracker = Tracker()
    tracker.load_saves()
    print(tracker.total_amount()) 

elif args.command == "summary-monthly":
    tracker = Tracker()
    tracker.load_saves()
    tracker.month_total(month= args.month)
    print(tracker.month_total(args.month))

elif args.command == "update":
    tracker = Tracker()
    tracker.load_saves()
    tracker.update_expense(
        index_user= args.index,
        field= args.field,
        new_value= args.new_value
    )
    tracker.save_expenses()