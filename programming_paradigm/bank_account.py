class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
        

    def deposit(self, amount):
        # Adds amount to account_balance
        self.account_balance += amount
        

    def withdraw(self, amount):
        #Checks if amount is more than account balance and deducts if it is less
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

        

    def display_balance(self):
        #Prints account_balance in 2 decimal places
        print("Current Balance: ${:.2f}".format(self.account_balance))
