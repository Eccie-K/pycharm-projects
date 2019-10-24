#create an account object
#states = accno, balance, type, branch, name
# behavior: deposit, withdrawal, buyairtime

class Account:
    def __init__(self, accno, balance, type, branch, name):

        self.accno = accno
        self.balance = balance
        self.type = type
        self.branch = branch
        self.name = name

    def deposit(self):
        amount = float(input("enter amount to deposit"))
        if amount <= 0:
            print("you cannot deposit zero or negative, retry")

        elif amount >= 70000:
            print("amount beyond recommended maximum limit")

        else:
            self.balance = self.balance + amount
            print("your deposited amount =", amount, "your balance is now:", self.balance)


    #withdrawal function
    #you cannot withdraw more than the balance
    #you cannot withdraw a zero or negative

    def withdrawal(self):
        amount = float(input("enter amount to withdraw"))
        if amount > self.balance:
            print("you do not have enough money in your account to withdraw the requested amount")

        elif amount <= self.balance:
            print("successfully withdrawn", amount)

        elif self.balance <= 0:
            print("your balance is zero, you cannot withdraw")

        else:
            self.balance = self.balance - amount
            print("amount withdrawn is", amount, "your available balance is", self.balance)



object = Account(accno = 123456, balance = 500, type = "savings", branch = "kenyatta", name = "ess")

object.deposit()
object.withdrawal()
