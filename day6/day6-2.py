import numpy



###########################################################################################
###########################################################################################
##################                                                         ################
##################                        NOT SOLVED                       ################
##################                                                         ################
###########################################################################################
###########################################################################################

with open("day6/input","r") as f:
    data = f.readlines()
data = [int(d) for d in data[0].split(',')]


#for testing
data = [3,4,3,1,2]
days = 256

map ={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,}

def load_map(map,data):
    for d in data:
        if d not in map:
            map[d]=0
        else:
            map[d]+=1      




load_map(map,data)
for day in range(days):
    print(f"Progress {(day/days)*100} %",end="\r")
    add_6=0
    add_8=0
    for _ in range(map[0]):
        add_6+=1
        add_8+=1
    map[0]=0
    
    for number in map:    
        if map[number]>0:
            for _ in range(map[number]):
                map[number]-=1
                map[number-1]+=1
                
    for _ in range(add_6):
        map[6]+=1
    for _ in range(add_8):
        map[8]+=1    
                      
    # print(f"AFTER  day{day}:")
    # for fish in map:
    #     print(f"{fish}:\t{map[fish]}")  

_sum = sum([map[fish] for fish in map])          
print("sum",_sum)    