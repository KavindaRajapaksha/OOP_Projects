class Customer:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
    
    def customer_details(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}"
    

class LoyaltyPoints:
    def __init__(self):
        self.loyalty_points = 0

    def earn_points(self,points):
        self.loyalty_points += points

    def redeem_points(self,points):
        if self.loyalty_points >= points:
            self.loyalty_points -= points
            
        else:
            print("Insufficient points to redeem")

    def show_points(self):
        return f"Loyalty Points: {self.loyalty_points}"

class VipCustomer(Customer,LoyaltyPoints):
    def __init__(self,customer_id,name):
        Customer.__init__(self,customer_id,name)
        LoyaltyPoints.__init__(self)
        self.discount = 10

    def show_discount(self):
        return f"Discount: {self.discount}%"
    
class Transaction:
    def __init__(self,customer,amount):
        self.customer = customer
        self.amount = amount

    def make_payment(self):
        if isinstance(self.customer,VipCustomer):
            discount = self.amount * self.customer.discount / 100
            amount = self.amount - discount
            print(f"Amount after discount: {amount}")
        else:
            amount = self.amount
            print(f"Amount: {amount}")

class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self,transaction):
        self.transactions.append(transaction)

    def show_transactions(self):
        for transaction in self.transactions:
            print(f"Customer: {transaction.customer.name}, Amount: {transaction.amount}")
        

vip = VipCustomer(1,"Alice")
vip.earn_points(100)
vip.show_points()
print(vip.show_discount())
