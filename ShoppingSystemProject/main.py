class User:
    def __init__ (self,username,email):
        self.username = username
        self.email = email


class Customer(User):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.cart = []

    def add_to_cart(self,product):
        self.cart.append(product)
        print(f"{product} added to cart")
    def remove_from_cart(self,product):
        if product in self.cart:
            self.cart.remove(product)
            print(f"{product} removed from cart")
        else:
            print(f"{product} not in cart")
    def view_cart(self):
        print("items in cart")
        for product in self.cart:
            print(product)
    def save_cart(self):
        with open(f"{self.username}_cart.txt","w") as file:
            for product in self.cart:
                file.write(product+"\n")
        print("cart saved")

class Seller(User):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.products = []
    def add_product(self,product):
        self.products.append(product)
        print(f"{product} added to products")
    def remove_product(self,product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product} removed from products")
        else:
            print(f"{product} not in products")
    def view_products(self):
        print("products in store")
        for product in self.products:
            print(product)
    def save_products(self):
        with open(f"{self.username}_products.txt","w") as file:
            for product in self.products:
                file.write(product+"\n")
        print("products saved")

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def basic_info(self):
        print(f"{self.name} costs {self.price}")



customer = Customer("john","user1@gmail.com")
seller = Seller("jane","seller1@gmail.com")
product1 = Product("laptop",1000)
product2 = Product("phone",500)
product3 = Product("tablet",300)

customer.add_to_cart(product1.name)
customer.add_to_cart(product2.name)
customer.add_to_cart(product3.name)
customer.view_cart()
customer.save_cart()


seller.add_product(product1.name)
seller.add_product(product2.name)
seller.add_product(product3.name)
seller.view_products()
seller.save_products()
