class Account:
    def __init__(self,acc_num,balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        if amount > self.balance:
            return 'Insufficient balance'
        self.balance -= amount
        return self.balance
    def get_balance(self):
        return self.balance
    


class InterestAccount(Account):
    def __init__(self,acc_num,balance,interest_rate):
        super().__init__(acc_num,balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate
    

class Transaction:
    def __init__ (self):
        self.transactions = []

    def add_transaction(self,transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        for transaction in self.transactions:
            print(transaction)

        

class SavingsAccount(InterestAccount,Transaction):
    def __init__ (self,acc_num,balance,interest_rate):
        InterestAccount.__init__(self,acc_num,balance,interest_rate)
        Transaction.__init__(self) 
    
    
savings = SavingsAccount(1234,1000,0.1)
savings.deposit(500)
savings.withdraw(200)
savings.calculate_interest()
savings.add_transaction('Deposit 500')
savings.add_transaction('Withdraw 200')
savings.get_transactions()
print(savings.get_balance())
        
        

    