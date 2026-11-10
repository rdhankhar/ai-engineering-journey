class student:
    
    # def __init__(self ,name = None ,cgpa = None ):
    #     if name is None:
    #         print("Hiii rahul ......")
    #     else:
    #         self.name = name
    #         self.cgpa = cgpa
    
    def __init__(self ,name,cgpa):
                self.name = name
                self.cgpa = cgpa
                
    def get_cgpa(self):
        return self.cgpa

# s = student() 
s1 = student("Rahul",8.5)
s2 = student("Karthik",10.0)
s3 = student("Gourav",9.0)

print(s1.name,s1.cgpa)
print(s2.name,s2.cgpa)
print(s3.name,s3.cgpa)
print(f"{s1.name} has cgpa = {s1.get_cgpa()}")
