import main

class Node:
    def __init__(self, element, manhattan, depth, prev, move):
        self.element = element
        self.depth = depth + 1
        self.priority = manhattan + self.depth
        self.prev = prev
        self.prevMove = move
    
class PriorityQueue:
    def __init__(self):
        self.queue = list()

    def insert(self, node):
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for x in range(0, len(self.queue)):
                if node.priority >= self.queue[x].priority:
                    if x == (len(self.queue)-1):
                        self.queue.insert(x+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) == 0

    def view(self):
        for x in range(len(self.queue)):
            print(self.queue[x].element, self.queue[x].priority)

def solver(board, k):
    visited = []
    depth = 0
    pq = PriorityQueue()
    pq.insert(Node(board, manhattan_value(board, k), depth, None, "Starting Position"))
    visited.append(board)

    iteration = 0
    while (not pq.isEmpty()):
        iteration += 1
        # pq.view()
        bestBoard = pq.dequeue() # Node Object
        # print("bestBoard")
        # main.printBoard(bestBoard.element, k)
        # print("Priority", bestBoard.priority)
        # print("Visited: ", visited)
        # print("\n")
        if (main.gameWon(bestBoard.element, k)):
            main.printBoard(bestBoard.element,k)
            print("Iterations: ", iteration)
            solution = []
            solution.append(bestBoard)
            while (bestBoard.prev != None):
                solution.append(bestBoard.prev)
                bestBoard = bestBoard.prev
            
            for x in range(len(solution)-1, -1,  -1):
                print(solution[x].prevMove)
                main.printBoard(solution[x].element, k)
            return

        else:
            if bestBoard.element not in visited:
                visited.append(bestBoard.element)
            legalMoves = main.moves(bestBoard.element, k)
            for move, offset in legalMoves.items():
                newBoard = bestBoard.element.copy()
                newBoard = main.swap(newBoard, move, k)
                if newBoard not in visited:
                    pq.insert(Node(newBoard, manhattan_value(newBoard, k), bestBoard.depth, bestBoard, move))


def manhattan_value(board, k):
    twodboard = TwoDBoard(board, k)
    goalBoard = correctBoard(k)
    
    score = 0

    for row in range(0, len(twodboard)):
        for column in range(0, len(twodboard[row])):
            value = twodboard[row][column]
            if value == "X":
                score += 0
            else:
                correct_coords = goalBoard[value]
                score += abs(correct_coords[1]-column) + abs(correct_coords[0]-row)

    return score

def TwoDBoard(board, k):
    twodboard = []
    for x in range(0, len(board), k):
        row = []
        for y in range(x, x+k):
            row.append(board[y])
        twodboard.append(row)
    return twodboard

def correctBoard(k):
    cBoard = {}
    tile = 1
    for x in range(0, k):
        for y in range(0, k):
            cBoard[tile] = [x,y]
            tile += 1
    del cBoard[k*k]
    return cBoard

            


