with open("day4/input","r") as f:
    data = f.readlines()

numbers=[int(d) for d in data[0].split(',')]
data = [line.strip('\n') for line in data[1:]]
print(numbers)
# print(data)

class Entry():
    def __init__(self,number):
        self.number=number
        self.marked=False

def extract_boards(data):
    ''' Return a 2d array with all the boards'''
    board=[]
    boards=[]
    for d in data:
        if d!='':
            # print("Row:",[int(i) for i in d.split()])
            board.append([Entry(int(i)) for i in d.split()])
        else:
            boards.append(board)
            board=[]
    boards.append(board)        
    return boards[1:]        


def check_bingo_row(row):
    streak=0
    for i,entry in enumerate(row):
        if entry.marked==True:
            streak+=1
            if streak == 5:
                return True            
    return False 

def check_bingo_col(board):
    for col in range(5):
        streak=0
        for row in board:
            if row[col].marked == True:
                streak+=1
                if streak == 5:
                    return True            
    return False            
                

def check_marker(row,n):
    for entry in row:
        if entry.number == n:
            entry.marked=True
            
def ger_marked(board):
    pass
def get_unmarked_sum(board):
    s=0
    for row in board:
        for entry in row:
            if entry.marked==False:
                s+=entry.number
    return s

def check_bingo(boards):
    winning_list=[]
    last_n=None
    max_boards=len(boards)
    winning_boards=0
    for n in numbers:
        for row in range(5):
            for i,board in enumerate(boards):
                check_marker(board[row],n)
                if check_bingo_col(board):
                    if i not in winning_list:
                        last_n=n
                        print(f"vertical bingo on board {i+1}! last number drawn was {n}")
                        winning_list.append(i)
                        winning_boards+=1
                    
                elif check_bingo_row(board[row]):
                    if i not in winning_list:
                        last_n=n
                        print(f"horizontal bingo on board {i+1}! last number drawn was {n}")
                        winning_list.append(i)
                        winning_boards+=1
                if winning_boards == max_boards:
                            
                    print(winning_list)
                    last_winning_board = boards[winning_list[-1]]
                    return(get_unmarked_sum(last_winning_board)*last_n)
                
                         
            

boards = extract_boards(data)
result = check_bingo(boards)
print(result)