class student:
    name = "Vinay"
    age = 10
    mark = 100
    
    def f():
        print("Hii ....")
    
s1 = student()

print("Name is : " , s1.name, "\n","Age is : " , s1.age, "\n","Mark is : ", s1.mark)

s2 = student()

s2.name = "Rahul"
s2.age = 21
s2.mark = 90

print("Name is : " , s2.name, "\n","Age is : " , s2.age, "\n","Mark is : ", s2.mark)

l = [1,2,3]
s = set()

student.f()

print(type(s1))

print(type(l))

print(type(s))