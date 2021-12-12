
with open("day7/input","r") as f:
    data = f.readlines()
crabs = [int(d) for d in data[0].split(',')]

# 327144 = fel

old_zum=None
record=None

for pos in range(min(crabs),max(crabs)+1):
    zum = sum([abs(crab_pos - pos) for crab_pos in crabs])
    if old_zum != None and zum < old_zum:
        record = zum
    old_zum = zum
    
print(record)    