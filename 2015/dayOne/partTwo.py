# 22/10/24 
floor = 0 
characterCount = 0 

with open("input.txt", "r") as file: 
    instructions = file.read() 

for step in instructions: 
    if step == "(": 
        characterCount+=1 
        floor = floor + 1 
    elif step == ")": 
        characterCount+=1
        floor = floor - 1
        if floor < 0: 
            print(characterCount)
            exit(0)

