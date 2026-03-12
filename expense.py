class Expenses:
    def __init__(self):
        self.name = ''
        self.value = float(0) 
        date

    def create_expense(self, name, value):
        self.name = name
        self.value = float(value)
           

    def __str__(self):
        return (f"{self.name}: {self.value} R$")
