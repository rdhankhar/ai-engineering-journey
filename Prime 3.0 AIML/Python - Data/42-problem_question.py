class Product:

    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    # instance method
    def get_info(self):
        print(f"Product {self.name} has price Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total product in store is : {cls.count}")

    @staticmethod
    def cal_discount(price, discount_percentage):
        print(f"Final price after discount is: {price - (price * discount_percentage / 100)}")
        
p1 = Product("Phone", 140000)
p2 = Product("Laptop", 50000)
p3 = Product("Watch", 40000)

p1.get_info()
Product.cal_discount(p1.price, 14)
Product.get_count()
