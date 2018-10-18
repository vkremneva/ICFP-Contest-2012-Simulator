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
            i, j = ind
            if not self.danger((i, j)):
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
        return abs(i1 - i2) + abs(j1 - j2)

    def is_goal_reached(self, current, goal):
        return current == goal

    def node_exists(self, i, j):
        if (i >= self.height) or (j >= self.width):
            return False
        return True

    def danger(self, possible_node):
        ip, jp = possible_node
        iR, jR = self.R

        small_maze = Maze()
        smsize = 5

        small_maze.width = smsize
        small_maze.height = smsize
        small_maze.maze = np.empty(shape=(smsize, smsize), dtype=str)
        smmid = smsize // 2
        small_maze.R = (smmid, smmid)

        for i in range(-smmid, smmid + 1, 1):
            for j in range(-smmid, smmid + 1, 1):
                if self.node_exists(iR + i, jR + j):
                    if self.maze[iR + i][jR + j] == '\\':
                        small_maze.lambdas.append((i + smmid, j + smmid))
                    small_maze.maze[i + smmid][j + smmid] = self.maze[iR + i][jR + j]
                else:
                    small_maze.maze[i + smmid][j + smmid] = '#'

        smpos = (smmid - iR + ip, smmid - jR + jp)
        small_maze.move_to(smpos)
        state = small_maze.update()

        if state == State.LOSE:
            return True

        return False

