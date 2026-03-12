import datetime

class Expenses:
    def __init__(self):
        self.name = ''
        self.value = float(0) 
        self.date = datetime.datetime(day=1, month=1, year=1)

    def create_expense(self, name, value, date):
        self.name = name
        self.value = float(value)
        self.date = date

    def __str__(self):
        return (f"{self.name}: {self.value} R$, {self.date}")
    

    

