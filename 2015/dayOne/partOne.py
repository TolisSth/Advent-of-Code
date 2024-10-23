# 22/10/24 
floor = 0 

with open("input.txt", "r") as file: 
    instructions = file.read() 

for step in instructions: 
    if step == "(": 
        floor = floor + 1 
    elif step == ")": 
        floor = floor - 1

print(floor)
