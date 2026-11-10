class Laptop:
        storage_type = "SSD"
    
        def __init__(self,RAM,ROM):
            self.RAM = RAM
            self.ROM = ROM
            
        @classmethod # Decorator
        def get_storage_type(cls):
            print(f"Storage type is : {cls.storage_type}")
            
        @staticmethod
        def cal_discount(price , discount):
            final_price = price - (discount * price / 100)
            print(f"Final price after discount is : {final_price}")
            
L1 = Laptop("16gb","512gb")
# L2 = Laptop("32gb","1024gb")

L1.cal_discount(400000 , 23)
