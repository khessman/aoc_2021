with open("day1/input.txt","r") as f:
    data = f.readlines()

data = [d.strip('\n') for d in data]
data = [int(d) for d in data]

cntr=0
for i in range(len(data)-1):
    if data[i+1] > data[i]:
        cntr+=1
print(cntr)   