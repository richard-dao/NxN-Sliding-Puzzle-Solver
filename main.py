import random
import math
def createGame(k):
    board = []
    for x in range(k*k-1):
        item = random.randint(1, (k*k-1))
        if item not in board:
            board.append(item)
        else:
            while item in board:
                item = random.randint(1, (k*k-1))
            board.append(item)
    
    blankIndex = random.randint(0, (k*k-1))
    board.insert(blankIndex, "X")
    return board

def checkValid(board, k):
    indexBlank = findBlank(board)
    if k % 2 == 1:
        board[indexBlank] = 9999
        inversions = numInversions(board) % 2 == 0
        board[indexBlank] = "X"

        return inversions
    else:
        row = math.floor(indexBlank / k ) + 1

        board[indexBlank] = 9999
        inversions = numInversions(board)
        board[indexBlank] = "X"

        if (row % 2 == 0):
            if (inversions % 2 == 0):
                return True
            return False
        else:
            if inversions % 2 == 1:
                return True
            return False

def findBlank(board):
    for x in range(len(board)):
        if board[x] == "X":
            return x
 
def numInversions(board):
    count = 0
    for x in range(len(board)):
        for y in range(x, len(board)):
            if (board[x] > board[y] and board[x] != 9999):
                count += 1
    return count

def printBoard(board, k):
    strBoard = "["
    for x in range(len(board)):
        if (x+1) % k == 0:
            if (x == len(board)-1):
                strBoard += str(board[x]) + "]"
            else:
                strBoard += str(board[x]) + "]\n["
        else:
            strBoard += str(board[x]) + " "
    print(strBoard)

def gameWon(board, k):
    for x in range(1, k*k):
        if board[x-1] != x:
            return False
    return True

def swap(board, move, k):
    legalMoves = moves(board, k) # Dictionary of legal moves and their offsets
    blankIndex = findBlank(board)

    if move in legalMoves:
        offSet = legalMoves[move]
        indexSwap = blankIndex + offSet

        temp = board[indexSwap]
        board[indexSwap] = "X"
        board[blankIndex] = temp
        return True
    else:
        return False


def moves(board, k):
    blankIndex = findBlank(board)
    blankCoords = indexToCoordinates(blankIndex, k)
    moveOffsets = {"U":-k,"D":k,"L":-1,"R":1}
    edgesLegal = edges(k)

    # We have legal moves for edges, if our blank index is on an edge,
    # we need to remove the ones not in their legal moves list

    if blankCoords in edgesLegal:
        legal = edgesLegal[blankCoords] # List of legal moves
        legalOffsets = {}
        for move in legal:
            legalOffsets[move] = moveOffsets[move]
        return legalOffsets
    else:
        return moveOffsets


    
def edges(k):
    edgesOffset = {(0,0):["R","D"],(0,k-1):["L","D"],(k-1,0):["R","U"],(k-1,k-1):["L","U"]}
    for r in range(0, k):
        for c in range(0, k):
            if r == 0 and (r,c) not in edgesOffset:
                edgesOffset[(r,c)] = ["D", "L", "R"]
            if r == k-1 and (r,c) not in edgesOffset:
                edgesOffset[(r,c)] = ["U", "L", "R"]
            if c == 0 and (r,c) not in edgesOffset:
                edgesOffset[(r,c)] = ["R", "U", "D"]
            if c == k-1 and (r,c) not in edgesOffset:
                edgesOffset[(r,c)] = ["L", "U", "D"]
    return edgesOffset

def indexToCoordinates(index, k):
    return ((index // k), (index % k))

            
k = 3
board = createGame(k)
while (checkValid(board, k) == False):
    board = createGame(k)
printBoard(board, k)

while (gameWon(board, k) == False):
    move = input("Move: ")
    if (move == "S"):
        print("Here's the solution!")
    while (swap(board, move, k) == False):
        if (move == "S"):
            print("Here's the solution")
            # solver()
            break
        else:
            move = input("Illegal Move, Try Again: ")
    printBoard(board, k)

print("You finished!")