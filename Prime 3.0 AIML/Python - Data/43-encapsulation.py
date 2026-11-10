class BankAccount:
    
    def __init__(self, name , balance):
        self.name = name 
        #self._balance = balance  Protected
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, newbalance):
            self.__balance = newbalance
    
acc1 = BankAccount("Rahul", 200000000000000)

acc1.set_balance(1400000)

# print(acc1.name , acc1.get_balance())
print(acc1.name , acc1._BankAccount__balance)