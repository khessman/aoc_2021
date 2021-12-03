with open("day2/input","r") as f:
    data = f.readlines()

instructions=list()
for line in data:
    dir,step = line.split(' ')
    instructions.append([dir,step])


h_pos=0
y_total=0
depth=0
aim=0

for i in instructions:
    if i[0] == "forward":   
        h_pos+=int(i[1])
        depth+=aim*int(i[1])
        
    # if i[0] == "backward":  h_pos-=int(i[1]) 
    if i[0] == "up":        
        # depth-=int(i[1])
        aim-=int(i[1])
        
    if i[0] == "down":      
        # depth+=int(i[1])
        aim+=int(i[1])


print(h_pos,depth,h_pos*depth)