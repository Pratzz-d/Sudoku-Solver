import random

def game_gen():
    f = open("d:\Programs\Python\Sudoku\sudoku.csv", "r")
    x = random.randrange(9000000)
    f.seek((x*164))
    game = f.readline(81)
    f.seek((x*164)+82)
    solution = f.readline(81)
    board = [[0 for i in range(9)]for j in range(9)]
    sol = [[0 for i in range(9)]for j in range(9)]
    k = 0
    for i in range(9):
        for j in range(9):
            board[i][j] = ord(game[k]) - 48 
            sol[i][j] = ord(solution[k]) - 48
            k+=1
    return(board,sol)