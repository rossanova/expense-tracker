from expense import Expense
import json

class Tracker:
    def __init__(self):
        self.expenses = [ ]

    def add_expense(self, expense):
        if isinstance(expense, Expense):
            self.expenses.append(expense)
            print(f"Expense added sucessfully (ID: {expense.id})")
        else:
            print("You must add an expense")
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
        try:
            index = int(index)
        except (ValueError, TypeError, IndexError):
            print("Not a right index value")
            return
        
        for expense in self.expenses:            
            if expense.id == index:
                self.expenses.remove(expense)
                print("Expense deleted sucessefully")
                return
        print("Expense not found")

    def update_expense(self, index_user, field, new_value):
        field = field.lower()

        for expense in self.expenses:
            if expense.id == index_user:
            
                if field == "description" :
                    try:
                        new_desc =  new_value.strip()
                        if new_desc == "" or new_desc == '':
                            print("Description cant be empty")
                            return
                        else: 
                            expense.description = new_desc
                            print("Expense sucessefully updated")
                            return
                    except (AttributeError, ValueError, TypeError):
                        print("Not a name")
                        return
                    
                elif field == "amount":
                    try:                        
                        updated_value = float(new_value)
                        if updated_value > 0:
                            expense.amount = updated_value
                            print("Expense sucessefully updated")
                            return
                        else:
                            print("Cant use negative number / zero")
                            return
                    except (ValueError, TypeError):
                        print("Thats not a number")
                        return
                else:    
                    print("Invalid Field")
                    return

        print("Invalid ID.")
            

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
        
        except (FileNotFoundError):
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


