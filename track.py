from expense import Expense
import datetime
import json

class Tracker:
    def __init__(self):
        self.expenses = [ ]

    def add_expense(self, expense):
        
        self.expenses.append(expense)


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
                return
            


    def update_expense(self, index_user, field, new_value):
        if 1 <= index_user and index_user <= len(self.expenses):
            index = index_user - 1
            
            expense = self.expenses[index]
        

            if field == "ID":
                expense.id = int(new_value)

            elif field == "Description" :
                expense.description = new_value.strip()
            
            elif field == "Amount" :
                expense.amount = float(new_value)

            elif field == "Date" :
                expense.date = datetime.datetime.strptime(new_value, "%d-%m-%Y")

            else:
                print("Invalid field.")

    def save_expenses(self):
        data = []
        for expense in self.expenses:
            data.append(expense.to_dict())
        with open ("expenses.json", "w") as f:
            json.dump(data, f)


    def load_saves(self):
        with open("expenses.json", "r") as f:
            data = json.load(f)

        self.expenses = [ ]

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
        return total

    def month_total(self, month):
        total = 0
        for expense in self.expenses:
            x = expense.date.split("-")
            mon = int(x[1])
            if mon == month:
                total += expense.amount
        return total

    def __str__(self):
        lines = [ ]
        for expense in self.expenses: 
            lines.append(str(expense))
        return "\n".join(lines)
            
'''
 r()
r = Expenses()
r.create_expense("Resenhinha", 40.30, datetime.datetime(2026, 3, 12) )
t.add_expense(r)
t.update_expense(1, "Value", 20.40) 
print(r.value)
'''