class student:
    
    college_name = "LPU"
    PI = 3.1
    
    def __init__(self ,name,cgpa):
                self.name = name
                self.cgpa = cgpa
                self.PI = 3.14
                
s1 = student("Rahul",8.5)
s2 = student("Karthik",10.0)
s3 = student("Gourav",9.0)

print(s1.name,s1.cgpa)
print(s2.name,s2.cgpa)
print(s3.name,s3.cgpa)
print(s1.PI)
print(student.PI)