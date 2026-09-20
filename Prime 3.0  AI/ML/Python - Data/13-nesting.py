# age = int(input("Enter age : "))

# if age >= 18:
#     print("Adult")
#     if age >= 18 and age <= 60:
#         print("He can drive")
#     else:
#         print("He can't drive")       
# else:
#     print("Not adult")    

username = input("Enter username : ")
password = int(input("Enter password : "))

if username == "Rahul" and password == 1150:
    print("Login Successful")
else :
    if username != "Rahul":
        print("Wrong username")
    else:
        print("Wrong password")        