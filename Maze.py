import numpy as np


class Maze:
    def __init__(self):
        self.maze = []
        self.acceptable_chars = ['R', '*', 'L', '.', '#', '\\', 'O', ' ']

    def read(self, fname):
        data = np.loadtxt(fname, dtype=str, delimiter='\n', comments=None, usecols=0)

        rows = 0
        for d in data:
            if (d[0] == '#') | (d[0] == 'L'):
                rows += 1

        self.maze = np.empty(shape=(rows, len(data[0])), dtype=str)
        for i in range(rows):
            for j, ch in enumerate(data[i]):
                if ch in self.acceptable_chars:
                    self.maze[i][j] = ch
                else:
                    print("Unacceptable char")  # todo

        return data, rows


newMaze = Maze()
newMaze.read("beard1.map")
