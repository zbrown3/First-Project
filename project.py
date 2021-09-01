from datetime import datetime



class Mortgage:
    
    def __init__(self, name, principal, interest, number_monthly_payments, property_tax, insurance):
        self.name = name
        self.principal = principal
        self.interest = interest
        self.number_monthly_payments = number_monthly_payments
        self.property_tax = property_tax
        self.insurance = insurance
        

    def __repr__(self):
        r = (self.interest / 100) / 12
        monthly_mortgage = str(round(self.principal * (r * (1 + r) ** self.number_monthly_payments) / ((1 + r) ** self.number_monthly_payments - 1) + (self.property_tax / 12) + (self.insurance / 12), 2))
        return "{}, based on your provided information, your estimated mortgage payment would be {} per month.".format(self.name,monthly_mortgage)

user = Mortgage(
    input("What is your full name? "),
    int(input("How much is the principal balance of the loan? ")),
    int(input("What is your interest rate in terms of percentage? ")),
    int(input("What is the length of your loan, 15 years or 30 years? ")),
    int(input("How much is your estimated annual property tax? ")),
    int(input("How much is your estimated homeowner's insurance? "))
)

print(user)

