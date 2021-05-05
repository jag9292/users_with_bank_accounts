class User:
    bank_name = "WatUp Bank"
    def __init__(self, email_address):
        self.email_address = email_address
        self.account = BankAccount
    def make_deposit(self, amount):
        self.account += amount
        print(self.account)
        return self
    def make_withdrawal(self, amount):
        self.account -= amount
        print(self.account)
        return self
    def display_user_balance(self):
        print("Your balance is:")
        print(self.account)
        return self

class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            print(self.balance)
        else:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        print(self.int_rate, self.balance)
        return self
    def yield_interest(self):
        interest = self.int_rate * self.balance        #500 * 0.02 = 10,
        self.balance= self.balance + interest              #500 - 10 = 490
        print(f"your balance is {self.balance}")
        return self

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

account1 = BankAccount(0.02, 0)
account2 = BankAccount(0.05, 0)


account1.display_account_info().deposit(100).deposit(50).deposit(100).deposit(80).withdraw(100).yield_interest().display_account_info()
account2.display_account_info().deposit(20).deposit(80).withdraw(10).withdraw(20).withdraw(20).withdraw(30).yield_interest().display_account_info()
