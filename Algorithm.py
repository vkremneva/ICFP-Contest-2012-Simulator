from astar import*
from Maze import*


class Algorithm(AStar, Maze):
    # (i, j) as node
    def neighbors(self, node):
        i, j = node
        available_neighbours = []
        neighbours = [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]
        next_neigh = [(i-2, j), (i, j-2), (i, j+2), (i+2, j)]
        uncond_acceptable_ch = ['.', '\\', 'O', ' ']
        cond_acceptable_ch = '*'

        for ind, n in zip(neighbours, next_neigh):
            if self.node_exists(*ind):
                i, j = ind
                if self.maze[i][j] in uncond_acceptable_ch:
                    available_neighbours.append(ind)
                elif self.maze[i][j] == cond_acceptable_ch:
                    inext, jnext = n
                    if self.node_exists(inext, jnext):
                        if self.maze[inext][jnext] == ' ':
                            available_neighbours.append(ind)

        return available_neighbours

    def distance_between(self, n1, n2):
        return 1

    def heuristic_cost_estimate(self, current, goal):
        i1, j1 = current
        i2, j2 = goal
        no_danger = abs(i1 - i2) + abs(j1 - j2)
        # return min(no_danger, self.danger(goal))
        return no_danger

    def node_exists(self, i, j):
        if (i >= self.height) | (j >= self.width):
            return False
        return True

    def danger(self, possible_node):
        death = -100
        i, j = possible_node

        if self.node_exists(i - 1, j):
            if self.maze[i - 1][j] == '*':
                return death
        if self.node_exists(i - 1, j - 1):
            if (self.maze[i - 1][j - 1] == '*') & \
                    ((self.maze[i][j - 1] == '*') | (self.maze[i][j - 1] == '\\')):
                return death
        if self.node_exists(i - 1, j + 1):
            if (self.maze[i - 1][j + 1] == '*') & (self.maze[i][j + 1] == '*'):
                return death

        return 1
