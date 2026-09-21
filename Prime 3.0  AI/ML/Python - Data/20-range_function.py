# odd , even , table numbers using range function

# for i in range(1,10,2):
#     print("Odd no. are :", i)

# for i in range(2,20 +1 ,2):
#     print("even no. are :", i)

# for i in range(18,180 + 1,18):
#     print("table of 18 is :", i)

n = int(input("Enter value of n :"))
sum = 0
for i in range(1 , n+1):
    sum += i
    
print("Sum of till 1 to", n ,"number is :",sum)