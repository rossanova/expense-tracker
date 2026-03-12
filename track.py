from expense import Expenses


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
        if index_user <= 1 and index_user <= len(self.list):
            index = index_user - 1
            
        expense = self.list[index]

        try:
            expense.value = float(x)
        except (ValueError, TypeError):
            expense.name = str(x).strip()
                                

    def __str__(self):
        lines = [ ]
        for expense in self.list: 
            lines.append(str(expense))
        return "\n".join(lines)
            

t = Tracker()
r = Expenses()
r.create_expense("Resenhinha", 40.30, (12, 3, 2026) )
t.add_expense(r)
t.update_expense(1, 30.40)
print(t) 