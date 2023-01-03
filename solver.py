
class Node:
    def __init__(self, element, manhattan, depth, prev):
        self.element = element
        self.depth = depth + 1
        self.priority = manhattan + self.depth
        self.prev = prev
    
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
            print(self.queue[x].element)

def solver(board, k):
    visited = []
    depth = 0
    pq = PriorityQueue()
    pq.insert(board, manhattan_value(board, k), depth, None)

    while (not pq.isEmpty()):
        bestBoard = pq.dequeue()
        


def manhattan_value(board, k):

