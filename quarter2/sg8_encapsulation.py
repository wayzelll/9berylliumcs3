class BankAccount:
    _counter = 0 #Sets the Account 

    def __init__(self, account_number, balance):
        BankAccount._counter += 1
        self._account_number = account_number
        self._balance = balance

        #Automatically shows the BankAccount
        print(f"Account {BankAccount._counter}")
        print(f"Account Number: {self._account_number}")
        print(f"Balance: {self._balance}")
  

    def get_balance(self):
        return self._balance


    def set_balance(self, value):
        print()
        print(f"Update balance to {value}")

        #Limits the value to numbers greater than 0 only
        if value < 0:
            print("The balance must be not be a negative number.")
        else:
            self._balance = value
            
        print(f"Account Number: {self._account_number}")
        print(f"Balance: {self._balance:.2f}\n")

    balance = property(get_balance, set_balance) #access the whole BankAccount

#Samples
a1 = BankAccount(12345, 1000)
a1.balance = -100
