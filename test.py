import main
import solver
k = 3
board = main.createGame(k)
while (main.checkValid(board, k) == False):
    board = main.createGame(k)
main.printBoard(board, k)

# board = [1,2,3,4,"X",6,7,5,8]

solvedState = None
while (main.gameWon(board, k) == False):
    move = input("Move: ")
    if (move == "S"):
        print("Here's the solution!")
        solver.solver(board, k)
        break
    while (main.swap(board, move, k) == False):
        if (move == "S"):
            print("\n Here's the solution!")
            solution = solver.solver(board, k)
        else:
            move = input("Illegal Move, Try Again: ")
    if main.gameWon(board, k):
        break
    main.printBoard(board, k)


print("You finished!")