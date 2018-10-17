from Algorithm import*


maze = Algorithm()
maze.read('maps\\contest6.map')
print(maze)

current = maze.R
while len(maze.lambdas) != 0:
    closest_lambda_ind = min(maze.lambdas, key=lambda x: maze.heuristic_cost_estimate(current, x))

    way = maze.astar(current, closest_lambda_ind)
    if way is None:
        print(State.LOSE)
        exit(1)

    next(way)
    wnext = next(way)
    state = maze.move_to(wnext)
    print('move:')
    print(maze)
    if state == State.WIN:
        print(state)
        exit(0)

    state = maze.update()
    print('update:')
    print(maze)
    if state == State.LOSE:
        print(state)
        exit(1)

    current = wnext
    print()

way = maze.astar(current, maze.exit)
next(way)
state = State.OK
while state != State.WIN:
    wnext = next(way)
    state = maze.move_to(wnext)
    if state == State.LOSE:
        print(state)
        exit(1)

    maze.update()
    print(maze)
