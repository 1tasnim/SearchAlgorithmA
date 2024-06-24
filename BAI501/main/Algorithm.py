import numpy as np
data = ""

class Node:
    def __init__(self, data, level, f_value):
        # Initialize the node with the data 
        self.data = data
        self.level = level
        self.f_value = f_value

    def generate_child(self):
        # Generate child nodes from the given node by moving the blank space
        x, y = self.findPath(self.data, '-')
        #  dashPosition contains position values for moving the blank space in either of the 4 directions [up,down,left,right] 
        dashPosition = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        children = []
        for i in dashPosition:
            child = self.swap(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level+1, 0)
                children.append(child_node)
        return children

    def swap(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            tempPuzzle = []
            tempPuzzle = self.clone(puz)
            temp = tempPuzzle[x2][y2]
            tempPuzzle[x2][y2] = tempPuzzle[x1][y1]
            tempPuzzle[x1][y1] = temp
            return tempPuzzle
        else:
            return None

    def clone(self, root):
        # create a similar matrix of the given node
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def findPath(self, puz, x):
        # Specifically used to findPath the position of the blank space 
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j

class PuzzleSolver:
    def __init__(self, size):
        # Initialize the puzzle 
        self.n = size
        self.openList = []
        self.closedList = []

    def f(self, start, goal):
        # Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) 
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        #  Calculates the different between the given puzzles 
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '-':
                    temp += 1
        return temp

    def search(self, start, goal):
        global data
        
        start = Node(start, 0, 0)
        start.f_value = self.f(start, goal)
        #  Put the start node in the openList list
        self.openList.append(start)
        print("\n\n")
        while True:
            cur = self.openList[0]
            print("Current State:")
            for i in cur.data:
                print(" | ", end="")
                for j in i:
                    print(j, end=" ")
                print("| ")
            data += "Current State:\n"
            for i in cur.data:
                data += " | "
                for j in i:
                    data += j + " "
                data += "| \n"
            data += "\n"

            # If the difference between current and goal node is 0 we have reached the goal node
            # break solve
            if self.h(cur.data, goal) == 0:
                print("\nGoal State Reached!")
                data += "\nGoal State Reached!"
                break
            for i in cur.generate_child():
                i.f_value = self.f(i, goal)
                self.openList.append(i)
            self.closedList.append(cur)
            del self.openList[0]
            self.openList.sort(key=lambda x: x.f_value, reverse=False)

def search_algorithm(start, goal):
    global data
    data = ""
    print(sorted(start))
    # check if start input from 1 to 8 with -
    if sorted(start) != ['-', '1', '2', '3', '4', '5', '6', '7', '8']:
        data = "Start: Input all unique numbers from 1 to 8 in any order with a - in between."
        return data
    # check if goal input from 1 to 8 with -
    elif sorted(goal) != ['-', '1', '2', '3', '4', '5', '6', '7', '8']:
        data = "Goal: Input all unique numbers from 1 to 8 in any order with a - in between."
        return data
    else:
        # convert array to 2d array
        start = np.reshape(start, (-1, 3))
        goal = np.reshape(goal, (-1, 3))
        try:
            # call puzzle function
            puz = PuzzleSolver(3)
            puz.search(start, goal)
        except:
            data = "Input Error !!!"
    return data