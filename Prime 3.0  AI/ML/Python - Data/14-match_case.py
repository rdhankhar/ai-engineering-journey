# color = input("Enter color : ")

# match color:
#     case "Red":
#         print("Stop")
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Look")
#     case _:
#         print("Wrong color ")

age = int(input("Enter age : "))

match age:
    case age if age < 18:
        print("Teenager")
    case age if age >= 18 and age <= 60:
        print("Adult")
    case age if age > 60 and age <= 100:
        print("Old")
    case _:
        print("Invalid age")