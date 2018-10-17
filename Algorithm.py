from astar import*
from Maze import*
from copy import deepcopy


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
            i, j = ind
            if self.maze[i][j] in uncond_acceptable_ch and \
                    not self.danger((i, j)):
                available_neighbours.append(ind)
            elif self.maze[i][j] == cond_acceptable_ch and \
                    not self.danger((i, j)):
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
        return abs(i1 - i2) + abs(j1 - j2)

    def is_goal_reached(self, current, goal):
        return current == goal

    def node_exists(self, i, j):
        if (i >= self.height) or (j >= self.width):
            return False
        return True

    def danger(self, possible_node):
        i, j = possible_node

        new_maze = deepcopy(self)
        new_maze.move_to((i, j))
        # print('move')
        # print(new_maze)
        state = new_maze.update()
        # print('update')
        # print(new_maze)
        # print()
        if state == State.LOSE:
            return True

        return False
