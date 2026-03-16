import datetime
import json
class Expense:
    def __init__(self, expense_id, description, amount, date):
        self.id = expense_id
        self.description = description
        self.amount = amount 
        self.date = date
    def to_dict(self):
        return { 
            "id" : self.id, 
            "description" : self.description,
            "amount": self.amount,
            "date": self.date
        }

    def __str__(self):
        return (f"Date: {self.date} | Description : {self.description} | Amount : {self.amount} | ID {self.id}")
    
