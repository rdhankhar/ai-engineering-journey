class Laptop:
        storage_type = "SSD"
    
        def __init__(self,RAM,ROM):
            self.RAM = RAM
            self.ROM = ROM
            
        @classmethod # Decorator
        def get_storage_type(cls):
            print(f"Storage type is : {cls.storage_type} {cls.RAM}")
            
L1 = Laptop("16gb","512gb")
L2 = Laptop("32gb","1024gb")

print(L1.get_storage_type())


