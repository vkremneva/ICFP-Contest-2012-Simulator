import numpy as np
from enum import Enum


class State(Enum):
    WIN = 0
    LOSE = -1
    OK = 1


class Maze:
    def __init__(self):
        self.maze = []
        self.acceptable_chars = ['R', '*', 'L', '.', '#', '\\', 'O', ' ']

    def __str__(self):
        lines = []
        for line in self.maze:
            lines.append(''.join(line))

        return '\n'.join(lines)

    def read(self, fname):
        data = np.loadtxt(fname, dtype=str, delimiter='\n', comments=None, usecols=0)
        # print(data)
        rows = 0
        for d in data:
            if (d[0] == '#') | (d[0] == 'L') | (d[0] == ' '):
                rows += 1

        max_len = len(max(*data, key=len))

        self.maze = np.empty(shape=(rows, max_len), dtype=str)
        for i in range(rows):
            for j, ch in enumerate(data[i]):
                if ch in self.acceptable_chars:
                    self.maze[i][j] = ch
                else:
                    raise ValueError("Unacceptable char in maze: " + ch)

        # print(self.maze)

    def update(self):
        height = len(self.maze)
        width = len(self.maze[0])
        rule1 = '* '
        rule2 = '* * '
        rule3 = ' * *'
        rule4 = '* \\ '
        fatal1 = '*R'
        fatal2 = ['* *R', ' *R*', '* \\R']

        for i in range(height-2, 0, -1):
            for j in range(0, width-1):
                neighbours = str(self.maze[i][j]) + str(self.maze[i][j+1]) + \
                             str(self.maze[i+1][j]) + str(self.maze[i+1][j+1])

                if (neighbours[0] == rule1[0]) & (neighbours[2] == rule1[1]):
                    self.maze[i][j] = ' '
                    self.maze[i+1][j] = '*'
                elif (neighbours[1] == rule1[0]) & (neighbours[3] == rule1[1]):
                    self.maze[i][j+1] = ' '
                    self.maze[i+1][j+1] = '*'
                elif neighbours == rule2:
                    self.maze[i][j] = ' '
                    self.maze[i+1][j+1] = '*'
                elif neighbours == rule3:
                    self.maze[i][j+1] = ' '
                    self.maze[i+1][j] = '*'
                elif neighbours == rule4:
                    self.maze[i][j] = ' '
                    self.maze[i+1][j+1] = '*'

                elif ((neighbours[0] == fatal1[0]) & (neighbours[2] == fatal1[1])) | \
                        ((neighbours[1] == fatal1[0]) & (neighbours[3] == fatal1[1])) | \
                        (neighbours in fatal2):
                    return State.LOSE

        return State.OK


maze = Maze()
maze.read('maps\\contest1.map')
print(maze)
print(maze.update())
print(maze)
