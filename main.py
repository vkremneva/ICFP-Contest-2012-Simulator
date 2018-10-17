from Algorithm import*

maze = Algorithm()
maze.read('maps\\contest5.map')
score = 0

current = maze.R
state = State.OK
while len(maze.lambdas) != 0:
    closest_lambda_ind = min(maze.lambdas, key=lambda x: maze.heuristic_cost_estimate(current, x))

    way = maze.astar(current, closest_lambda_ind)
    wnext = ()

    if way is None:
        state = State.WIN
        print(state)
        print('score:', score)
        exit(0)
    else:
        next(way)

    if way is None:
        state = State.WIN
        print(state)
        print('score:', score)
        exit(0)
    else:
        wnext = next(way)

    state, new_score = maze.move_to(wnext)
    score = score - 1 + new_score
    # print('move:')
    # print(maze)
    if state == State.WIN:
        break

    state = maze.update()
    # print('update:')
    # print(maze)
    if state == State.LOSE:
        break

    current = wnext
    # print()

if state != State.OK:
    print(state)
    print('score:', score)
    exit(0)

way = maze.astar(current, maze.exit)
state = State.OK
wnext = ()

if way is None:
    state = State.WIN
    print(state)
    print('score:', score)
    exit(0)
else:
    next(way)

if way is None:
    state = State.WIN
    print(state)
    print('score:', score)
    exit(0)
else:
    wnext = next(way)

while state != State.WIN:
    if way is None:
        state = State.WIN
        break
    else:
        wnext = next(way)

    state, new_score = maze.move_to(wnext)
    score = score - 1 + new_score
    if state != State.OK:
        break

    maze.update()
    print(maze)

if state != State.OK:
    print(state)
    print('score:', score)
    exit(0)
