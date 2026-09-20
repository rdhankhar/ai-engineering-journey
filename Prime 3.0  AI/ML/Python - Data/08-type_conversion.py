# Type conversion and casting is a implicit or automatic which is done by the python.

# a = 10
# # b = 20.5
# b = 20
# print(type(a+b))
# print(type(a/b))

# Type casting ia a explicit or manually done by the user.

a = int(10 + 20.5)
b = float(10 + 20)
c = bool(10)
d = bool(0)
e = int("123")

print(a,(type(a)))
print(b,(type(b)))
print(c,(type(c)))
print(d,(type(d)))  
print(e,(type(e)))