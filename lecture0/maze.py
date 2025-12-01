import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state 
        self.parent = parent
        self.action = action 

class StackFrontier():
    def __init__ (self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == node for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class Queuefrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze():
    def __init__(self, filename):
        with open(filename) as file:
            contents = file.read()
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == 'A':
                        self.stats(i,j)
                        row.append(False)
                    elif contents[i][j] == 'B':
                        self.goal(i,j)
                        row.append(False)
                    elif contents[i][j] == ' ':
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None

