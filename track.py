from expense import Expense
import datetime
import json

class Tracker:
    def __init__(self):
        self.expenses = [ ]

    def add_expense(self, expense):
        self.expenses.append(expense)
        print(f"Expense added sucessfully (ID: {expense.id})")

    def next_id(self):
        if len(self.expenses) < 1:
            return 1
        else:
            x = [ ]
            for expenses in self.expenses:
                x.append(expenses.id)
                x.sort()
            return x[-1] + 1  

    def delete_expense(self, index):
        for expense in self.expenses:
            if expense.id == index:
                self.expenses.remove(expense)
                return print("Expense deleted sucessefully")
            


    def update_expense(self, index_user, field, new_value):
        for expense in self.expenses:
            if expense.id == index_user:
            
                if field == "Description" :
                    expense.description = new_value.strip()


                elif field == "Amount" :
                    expense.amount = float(new_value)

                else:
                    print("Invalid field.")
            else:
                print("Invalide ID")
            

    def save_expenses(self):
        data = []
        for expense in self.expenses:
            data.append(expense.to_dict())
        with open ("expenses.json", "w") as f:
            json.dump(data, f)


    def load_saves(self):
        try:
            with open("expenses.json", "r") as f:
                data = json.load(f)
        
        except FileNotFoundError:
            print("There is nothing to load")
            self.expenses = []
            return

        self.expenses = []

        for expenses in data:
            e = Expense(
                expenses["id"],
                expenses["description"],
                expenses["amount"],
                expenses["date"]
        )
            self.expenses.append(e)
    


    def total_amount(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return print(f"Total expenses: {total}")

    def month_total(self, month):
        total = 0
        for expense in self.expenses:
            x = expense.date.split("-")
            mon = int(x[1])
            if mon == month:
                total += expense.amount

        return print(f"Total expenses for {month}: {total}")

    def list_expenses(self):
        lines = ["ID   DATE   DESCRIPTION   AMOUNT" ]
        for expense in self.expenses:
            line = f"{expense.id}, {expense.date}, {expense.description}, {expense.amount}$ "
            lines.append(line)
        return "\n".join(lines)
    def __str__(self):
        lines = []
        for expense in self.expenses: 
            lines.append(str(expense))
        return "\n".join(lines)

