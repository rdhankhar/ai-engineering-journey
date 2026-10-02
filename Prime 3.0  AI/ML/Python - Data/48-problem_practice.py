# Finding word
data = True
line = 1
word = "pythonn"

with open("sample.txt", "r") as f:
    
    while data:
        data = f.readline()
        
        if word in data:
            print(f"{word} found at line {line}")
        else:
            print(f"{word} not exist in file")
            break
        line += 1