from expense import Expenses
import datetime

class Tracker:
    def __init__(self):
        self.list = [ ]

    def add_expense(self, expense):
        self.list.append(expense)

    def delete_expense(self, index_user):
        if index_user >= 1 and index_user <= len(self.list):
            index = index_user - 1
            self.list.pop(index)

    def update_expense(self, index_user, x):
        if 1 <= index_user and index_user <= len(self.list):
            index = index_user - 1
            
            expense = self.list[index]

            try:
                expense.value = float(x)
                return
            except ValueError:
                pass
                try:
                    expense.date = datetime.datetime.strptime(x, "%Y-%m-%d")
                    return
                except ValueError:
                    pass
                try:
                    expense.date = datetime.datetime.strptime(x, "%Y-%m-%d")
                    return
                except ValueError:
                    expense.name = str(x).strip()
                    return



    def __str__(self):
        lines = [ ]
        for expense in self.list: 
            lines.append(str(expense))
        return "\n".join(lines)
            
"""
t = Tracker()
r = Expenses()
r.create_expense("Resenhinha", 40.30, datetime.datetime(2026, 3, 12) )
t.add_expense(r)
t.update_expense(1, 30.40)
print(r.date.year) 
"""