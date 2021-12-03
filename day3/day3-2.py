with open("day3/input","r") as f:
    data = f.readlines()
data = [d.strip('\n') for d in data]


def get_mcv_o2(data,index):
    total = sum( [ int(b[index]) for b in data ])
    half = len(data)/2
    if total > half: return 1
    if total < half: return 0
    if total == half: return 1

def get_mcv_co2(data,index):
    total = sum( [ int(b[index]) for b in data ])
    half = len(data)/2
    if total > half: return 0
    if total < half: return 1
    if total == half: return 0



def find_rating(rating,data,index):
    
    if len(data)==1:
        return data
    else:
        if rating=="co2":
            mcv = get_mcv_co2(data,index)
        if rating=="o2":
            mcv = get_mcv_o2(data,index)    
        data2=[]
        for i in range(len(data)):
            if int(data[i][index])==mcv:
                data2.append(data[i])
        return find_rating(rating,data2,index+1)             


a=find_rating("o2",data,index=0)
b=find_rating("co2",data,index=0)
a = ( int("".join(str(d)for d in a),base=2) )
b = ( int("".join(str(d)for d in b),base=2) )

print(a,b,a*b)
