# object to show a bank account
class Account:

    def __init__(self, account_number, account_name, account_type, branch):
        self.account_number = account_number
        self.account_name = account_name
        self.account_type = account_type
        self.branch = branch


    def deposit(self):
        amount_deposited = int(input("enter amount"))
        amount_withdrawn = int(input("enter amount to withdraw"))
        account_balance = amount_deposited - amount_withdrawn

        print("your deposit is:", amount_deposited)
        print("amount withdrawn is:", amount_withdrawn)
        print("account balance is:", account_balance)




    def state(self):
        print("your account name is:", self.account_name)
        print("your account_number is:", self.account_number)
        print("your account type is:", self.account_type)
        print("your branch is:", self.branch)



object = Account(account_number = 15487906, account_name = "julia Kitony", account_type = "savings account", branch = "nairobi",  )

object.deposit()
object.state()


