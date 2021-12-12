
with open("day6/input","r") as f:
    data = f.readlines()
data = [int(d) for d in data[0].split(',')]

#for testing
data = [3,4,3,1,2]   
days=18



def produce_fish(group):
    add_fish=0
    for fish in range(len(group)):
        if group[fish]==0:
            add_fish+=1
            group[fish]=6
        else:
            group[fish]-=1
                
    for i in range(add_fish):
        group.append(8)        
    return group    



for i in range(days):
    data = produce_fish(data)
    print(f"After {i+1} days: {data}")
print(f"After {days} days there are {len(data)} fish")    