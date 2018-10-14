import numpy as np


class Maze:
    def __init__(self):
        self.maze = []
        self.acceptable_chars = ['R', '*', 'L', '.', '#', '\\', 'O', ' ']

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
