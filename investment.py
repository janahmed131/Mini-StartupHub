class Investment:

    def __init__(self, investor, project, amount, date):  

        self.investor = investor 
        self.project = project
        self.amount = amount
        self.date = date

    def to_dict(self):   

        return {
            "investor": self.investor,
            "project": self.project,
            "amount": self.amount,
            "date": self.date
        }
