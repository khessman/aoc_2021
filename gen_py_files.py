import os

for i in range(1,25,1):
    if not os.path.exists(f"day{str(i)}"):
        os.mkdir(f"day{str(i)}")
        if not os.path.exists(f"day{i}/day{i}-1.py"):
            f = open(f"day{i}/day{i}-1.py","w")
            f.close()
            f = open(f"day{i}/day{i}-2.py","w")
            f.close()