import numpy as np
from enum import Enum


class State(Enum):
    WIN = 0
    LOSE = -1
    OK = 1


class Maze:
    def __init__(self):
        self.maze = []
        self.lambdas = []
        self.R = (0, 0)
        self.exit = (0, 0)
        self.height = 0
        self.width = 0
        self.acceptable_chars = ['R', '*', 'L', '.', '#', '\\', 'O', ' ']

    def __str__(self):
        lines = []
        for line in self.maze:
            lines.append(''.join(line))

        return '\n'.join(lines)

    def read(self, fname):
        data = np.loadtxt(fname, dtype=str, delimiter='\n', comments=None, usecols=0)
        # print(data)
        for d in data:
            if (d[0] == '#') | (d[0] == 'L') | (d[0] == ' '):
                self.height += 1

        self.width = len(max(*data, key=len))

        self.maze = np.empty(shape=(self.height, self.width), dtype=str)
        for i in range(self.height):
            for j, ch in enumerate(data[i]):
                if ch in self.acceptable_chars:
                    self.maze[i][j] = ch
                    if ch == '\\':
                        self.lambdas.append((i, j))
                    elif ch == 'L':
                        self.exit = (i, j)
                    elif ch == 'R':
                        self.R = (i, j)
                else:
                    raise ValueError("Unacceptable char in maze: " + ch)

        # print(self.maze)

    def update(self):
        rule1 = '* '
        rule2 = '* * '
        rule3 = ' * *'
        rule4 = '* \\ '
        fatal1 = '*R'
        fatal2 = ['* *R', ' *R*', '* \\R']

        for i in range(self.height-2, 0, -1):
            for j in range(0, self.width-1):
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

    def move_to(self, dest):
        state = State.OK
        wall = False
        score = 0
        i, j = self.R

        destinations = {'U': (i-1, j), 'D': (i+1, j), 'L': (i, j-1), 'R': (i, j+1)}
        if dest in destinations.values():
            idest, jdest = dest
            if self.maze[idest][jdest] == '\\':
                score += 25
                self.lambdas.remove(dest)
                if len(self.lambdas) == 0:
                    ie, je = self.exit
                    self.maze[ie][je] = 'O'

            elif self.maze[idest][jdest] == '*':
                if dest == destinations['U']:
                    self.maze[idest+1][jdest] = '*'
                elif dest == destinations['D']:
                    self.maze[idest-1][jdest] = '*'
                elif dest == destinations['L']:
                    self.maze[idest][jdest-1] = '*'
                elif dest == destinations['R']:
                    self.maze[idest][jdest+1] = '*'

            elif self.maze[idest][jdest] == '#':
                wall = True

            elif self.maze[idest][jdest] == 'O':
                state = State.WIN
                score += 50

            if not wall:
                self.R = dest
                self.maze[idest][jdest] = 'R'
                self.maze[i][j] = ' '

        return state, score
