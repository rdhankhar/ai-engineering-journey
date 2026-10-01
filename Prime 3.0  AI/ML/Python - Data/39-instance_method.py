class Laptop:
        storage_type= "SSD"
    
        def __init__(self,RAM,ROM):
            self.RAM = RAM
            self.ROM = ROM
        
        def get_info(self):
            print(f"Laptop has {self.RAM} RAM and {self.ROM} ROM and storage type is : {Laptop.storage_type}")
            
L1 = Laptop("16gb","512gb")
L2 = Laptop("32gb","1024gb")

print(L1.get_info())
print(L2.get_info())