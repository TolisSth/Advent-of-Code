#23/10/24
total = 0 

with open("input", "r") as file: 
    dimensions = file.readlines() 

for line in dimensions: 
     clean_line = line.strip() 
     lwh = clean_line.split('x')
     l = int(lwh[0]) 
     w = int(lwh[1])
     h = int(lwh[2])
    
     sides = [ 2*l*w, 2*w*h, 2*h*l]
     smallest_side = sorted(sides)
     
     formula = sum(sides) + smallest_side[0]/2
     print(formula)
     total = total + int(formula)

print(total)
