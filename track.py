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

    def update_expense(self, index_user):
        if index_user <= 1 and index_user <= len(self.list):
            index = index_user - 1


    def __str__(self):
        lines = [ ]
        for expense in self.list: 
            lines.append(str(expense))
        return "\n".join(lines)
            

t = Tracker()
r = Expenses()
r.create_expense("Rafael", "15")
t.add_expense(r)
print(t)
