import random

def CheckValid(grid,row,col,num):
    valid = True
    for x in range (9):
        if(grid[x][col] == num):
            valid = False
    
    for y in range (9):
        if(grid[row][y] == num):
            valid = False 
    
    rownum = row//3
    colnum = col//3
    for x in range (3):
        for y in range (3):
            if(grid[rownum*3 + x][colnum*3 + y] == num):
                valid = False
    return valid

def MakeBoard():
    board = [[0 for i in range (9)]for j in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = 0
    for i in range(25):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,9)
        while(not CheckValid(board,row,col,num) or board[row][col] != 0):
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,9)
        board[row][col] = num
    print()
    for i in range(len(board)):
        if i%3==0 and i!=0 :
            print("-  -  -  -  -  -  -  -  -  -  -  -  -")
        for j in range(len(board[0])):
            if j%3==0 :
                print("| ",end =" ")
            if j==8:
                print(str(board[i][j]) +"  | ")
            else : 
                print(str(board[i][j]) + " ",end=" ")
    print()

MakeBoard()