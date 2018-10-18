from Algorithm import*

maze = Algorithm()
maze.read('maps\\contest5.map')
score = 0

# gather lambdas
current = maze.R
state = State.OK
while len(maze.lambdas) != 0:
    closest_lambda_ind = min(maze.lambdas, key=lambda x: maze.heuristic_cost_estimate(current, x))

    way = maze.astar(current, closest_lambda_ind)
    wnext = ()

    if way is None:
        state = State.WIN
        break
    else:
        try:
            next(way)
            wnext = next(way)
        except StopIteration:
            state = State.WIN
            break

    state, new_score = maze.move_to(wnext)
    score = score - 1 + new_score
    if state == State.WIN:
        break

    state = maze.update()
    if state == State.LOSE:
        break

    current = wnext

if state != State.OK:
    print(state)
    print('score:', score)
    exit(0)

# going outside
way = maze.astar(current, maze.exit)
wnext = ()

if way is None:
    state = State.WIN
    print(state)
    print('score:', score)
    exit(0)
else:
    try:
        next(way)
        wnext = next(way)
    except StopIteration:
        state = State.WIN
        print(state)
        print('score:', score)
        exit(0)

while state != State.WIN:
    if way is None:
        state = State.WIN
        break
    else:
        try:
            wnext = next(way)
        except StopIteration:
            state = State.WIN
            break

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
