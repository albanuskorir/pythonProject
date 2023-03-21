import datetime

class Bank_Account:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer name:", self.customer_name)
        print("Account number:", self.account_number)
        print("Date of account opening:", self.date_of_opening)
        print("Current balance:", self.balance)

# Example usage
account = Bank_Account("1234567890", 35000, datetime.date(2023, 3, 15), "Albert Kamau")
print("Amount deposited:", account.deposit(5000))
print("Amount withdrawn:", account.withdraw(50000))
account.check_balance()
account.customer_details()
