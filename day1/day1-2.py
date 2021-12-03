with open("day1/input.txt","r") as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]
data = [int(d) for d in data]

last_ma3=0
cntr=0
for i in range(len(data)-3):
    ma3 = sum(data[i:i+3])
    
    if ma3 > last_ma3:
        cntr+=1
    
    last_ma3=ma3
    
print(cntr)