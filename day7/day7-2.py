
with open("day7/input","r") as f:
    data = f.readlines()
crabs = [int(d) for d in data[0].split(',')]

old_zum=None
record=None


# using https://en.wikipedia.org/wiki/Triangular_number
# to speed up the sum of the numbers.

# d=abs(16 - 5)
# triangular = d * (d+1) // 2
# print(triangular)

print(f"Largest postition: {max(crabs)}")

for pos in range(min(crabs),max(crabs)+1):
    
    zum = sum([abs(crab_pos - pos) * (abs(crab_pos - pos)+1) // 2 for crab_pos in crabs])
    if old_zum != None and zum < old_zum:
        record = zum
    old_zum = zum
    
print("Smallest",record)    