with open("day3/input","r") as f:
    data = f.readlines()
data = [d.strip('\n') for d in data]


gamma=[0]*len(data[0])
epsilon=[0]*len(data[0])


for i in range(len(data[0])):
    gamma[i] = 1 if sum( [ int(b[i]) for b in data ]) > (len(data) / 2) else 0
    epsilon[i] = 0 if sum( [ int(b[i]) for b in data ]) > (len(data) / 2) else 1

gamma = ( int("".join(str(d)for d in gamma),base=2) )

epsilon = ( int("".join(str(d)for d in epsilon),base=2) )

print(gamma,epsilon,gamma*epsilon)