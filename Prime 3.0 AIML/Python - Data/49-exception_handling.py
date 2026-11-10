try:
    x = int(input("Enter x value : "))
    ans = 10/x
    
except ZeroDivisionError:
    print("Divide by zero is not allowed")
    
except ValueError:
    print("Invalid Value")
    
else:
    print(f"Ans is : {ans}")
    
finally:
    print("End of program")