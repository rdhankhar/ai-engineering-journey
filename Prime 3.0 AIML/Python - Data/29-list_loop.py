# l = [10,15,18,40,43,32]

# for var in l:
#     print(type(var))

#sum 

# l = [10,15,18,40,43,32]

# sum = 0

# for var in l:
#     sum += var
    
# print("Sum is :", sum)   

# Linear search

l = [10,15,18,40,43,32]

x = 40
idx = 0
for var in l:
    if(var == x):
        print(f"{x} is at index {idx}")
        break
    idx += 1



