with open("day5/input","r") as f:
    data = f.readlines()
GRIDSIZE_X = 1000
GRIDSIZE_Y = 1000
#create grid(base this on max size, 10x10 is enough for example)
grid = [[0 for _ in range(GRIDSIZE_X)] for _ in range(GRIDSIZE_Y)]



def show_grid():
    for g in grid:
        print(g)
    print()    
        
        
def place_straight(a,b):
    # print(f"Placing {a} to {b} ")
    #place into grid
    x1=a[0] if a[0] < b[0] else b[0]
    x2=b[0] if a[0] < b[0] else a[0]
    y1=a[1] if a[1] < b[1] else b[1]
    y2=b[1] if a[1] < b[1] else a[1]
      
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            grid[y][x]+=1      

def place_diagonal(a,b):
    # print(f"Placing {a} to {b} ")
    #place into grid
    x1=a[0]
    x2=b[0]
    y1=a[1]
    y2=b[1]
    x_step= -1 if x1 > x2 else 1 
    y_step= -1 if y1 > y2 else 1 
      
    while x1 != x2+x_step and y1 != y2+y_step:
        grid[y1][x1]+=1
        x1+=x_step
        y1+=y_step
    # show_grid()     

def count_overlaps(grid):
    cntr=0
    for y in range(GRIDSIZE_Y):
        for x in range(GRIDSIZE_X):
            if grid[y][x] > 1:
                cntr+=1
    return cntr            



# data = ["8,0 -> 0,8"]
#parse positional data and place on grid, increment number if number pos in grid is already occupied.
for line in data:
    #parse line and convert into A and B list with posdata
    a,_,b = line.partition(" -> ")
    a = [int(x) for x in a.split(',')]
    b = [int(x) for x in b.split(',')]
    
    #horizontal and vertical lines
    if a[0]==b[0] or a[1]==b[1]:
        place_straight(a,b)
        pass
    else:
        place_diagonal(a,b)
        pass
        

# show_grid()    


#scan grid and count positions with number higher than 1
result = count_overlaps(grid)
print(result)