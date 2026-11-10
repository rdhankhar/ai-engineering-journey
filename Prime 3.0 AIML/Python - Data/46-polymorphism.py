# class teacher:
#     def get_designation(self):
#         print("Designation : teacher")
        
# class student(teacher):
#     def get_designation(self):
#         print("Designation : student")

# s1 = student()

# print(s1.get_designation())

# duck type polymorphism

class teacher:
    def get_designation(self):
        print("Designation : teacher")
        
class student:
    def get_designation(self):
        print("Designation : student")

t1 = teacher()
print(t1.get_designation())

s1 = student()
print(s1.get_designation())



