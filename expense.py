class Expenses:
    def __init__(self):
        self.name = ''
        self.value = int(0) 

    def create_expense(self, name, value):
        self.name = name
        self.value = int(value)
           

    def __str__(self):
        return (f"{self.name}: {self.value} R$")