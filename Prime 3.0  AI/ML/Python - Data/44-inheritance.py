# Single inheritance 

class Manager:
    start_time = "10:00 AM"
    end_time = "5:00 PM"
    
class Employee(Manager): 
    def __init__(self, name ):
        self.name = name 
        
E1 = Employee("Rahul")

print(E1.name, E1.start_time,E1.end_time)

# Multilevel inheritance 

class Manager:
    start_time = "10:00 AM"
    end_time = "5:00 PM"
    
class Employee(Manager): 
    def __init__(self, name ):
        self.name = name 
        
class Accountant(Employee):
    
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary
        
a1 = Accountant("Rahul",200000)

print(a1.name,a1.salary, a1.start_time,a1.end_time)
    
    
# Multiple inheritance 

class Teacher:
    start_time = "10:00 AM"
    end_time = "5:00 PM"
    
class Student: 
    def __init__(self, name ):
        self.name = name 
        
class Specialization:
    def __init__(self, role ):
            self.role = role
            
class Result(Teacher,Student,Specialization):
    def __init__(self,name,role,cgpa):
        super().__init__(name)
        Specialization.__init__(self,role)
        self.cgpa = cgpa
        
s1 = Result("Rahul","AI Engineer",9.0)

print(s1.name,s1.role, s1.cgpa,s1.start_time,s1.end_time)