# read mode 
# f = open("sample.txt")
# f = open("sample.txt", "r")

# data = f.readline()

# print(data)

# data = f.readline()

# print(data)
# print(f.read())

# # write mode 
# f = open("sample.txt", "w")

# # f.write("Hii 123")

# f.close()

# Append mode = It will add the text at the back without ny truncate
# f = open("sample.txt", "a")

# f.write("\n it's me rahul")

# f.close()

# x mode to add a new text file 

# f = open("sample.txt 2", "x")

# f.write("Hii what's up")

# f.close()

# f = open("sample.txt 3", "x")

# f.write("Hiiii")

# f.close()

# # r+ = It will read and write but it can overwrite the text from the begining

# f = open("sample.txt", "r+")

# f.write("001")

# print(f.read())
# f.close()

# # w+ = It will read and write but it can truncate all the text of the file 

# f = open("sample.txt", "w+")

# f.write("001")

# print(f.read())
# f.close()

# a+ = It will read and append but it can add text from the end 

# f = open("sample.txt 2", "a+")

# f.write("\n I'm learning python \n from apna college. ")

# print(f.read())
# f.close()

# With keyword

# with open("sample.txt 2", "r") as f:

#     data = f.read()
#     print(len(data))
#     print(data)

# delete files

import os 

os.remove("sample.txt 3")





