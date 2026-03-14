from expense import Expenses
import datetime
import json

class Tracker:
    def __init__(self):
        self.list = [ ]

    def add_expense(self, expense):
        
        self.list.append(expense)


    def delete_expense(self, index_user):
        if index_user >= 1 and index_user <= len(self.list):
            index = index_user - 1
            self.list.pop(index)

    def update_expense(self, index_user, field, new_value):
        if 1 <= index_user and index_user <= len(self.list):
            index = index_user - 1
            
            expense = self.list[index]
        

            if field == "Name" :
                expense.name = new_value.strip()
            
            elif field == "Value" :
                expense.value = float(new_value)

            elif field == "Date" :
                expense.date = datetime.datetime.strptime(new_value, "%d-%m-%Y")

            else:
                raise NameError
    def save_expenses(self, data):
        data = [ ]
        for expense in self.list:
            data.append(expense.dictionary())
        with open("expenses.json", "w") as f:
            json.dump(data, f)

    def load_saves(self):
        with open("expenses.json", "r") as f:
            dados = json.load(f)
            
        self.list = [ ]

        for expenses in dados:
            e = Expenses(expenses)
            e.name = expenses["name:"]
            e.value = expenses["value:"]
            e.date = expenses["date:"]
            self.list.append(e)
    
    
    def __str__(self):
        lines = [ ]
        for expense in self.list: 
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