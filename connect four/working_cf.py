from dataclasses import replace
grid = [[0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7]

def board():
    print(" c1 c2 c3 c4 c5 c6 c7")
    for row in grid:
        print(f'[{", ".join([str(i)for i in row])}]') # formating the grid

def move1(col):
    for i in range(5,-1,-1):
        if grid[i][col] == 0:
            grid[i][col] = 1
            return True
    return False
        
def move2(col):
    for j in range(5,-1,-1):
        if grid[j][col] == 0:
            grid[j][col] = 2
            return True
    return False

while True:
    #player 1
    board() # prints at the start and updates after Player2 turn
    player1 = input("Player1 move: ")
    if player1 == "n": break
    colIndex = int(player1[1])-1
    if colIndex < 0 or colIndex > 6: continue
    print(move1(colIndex))
    board() # updates player1 turn
    #Player 2
    player2 = input("Player2 move: ")
    if player2 == "n": break
    colIndex = int(player2[1])-1
    if colIndex < 0 or colIndex > 6: continue
    print(move2(colIndex)) 
    