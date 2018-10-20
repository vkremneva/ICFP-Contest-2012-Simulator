from Algorithm import*

maze = Algorithm()
maze.read('maps\\contest6.map')
score = 0
amount_of_steps_to_remember = 3
unreachable_lambdas = []
last_steps = []

# gather lambdas
current = maze.R
state = State.OK
while len(maze.lambdas) != 0:
    # print(maze)
    # print()
    closest_lambda_ind = min(maze.lambdas, key=lambda x: maze.heuristic_cost_estimate(current, x))

    way = maze.astar(current, closest_lambda_ind)
    wnext = ()

    if way is None or type(way) == list:
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
    if new_score == 25 and len(unreachable_lambdas) != 0:
        maze.lambdas.append(unreachable_lambdas.pop())
    # print(maze)
    score = score - 1 + new_score
    if state == State.WIN:
        break

    state = maze.update()
    if state == State.LOSE:
        break

    current = wnext

    if len(last_steps) != amount_of_steps_to_remember:
        last_steps.append(wnext)
    else:
        if last_steps[0] == last_steps[2]:
            unreachable_lambdas.append(closest_lambda_ind)
            if closest_lambda_ind in maze.lambdas:
                maze.lambdas.remove(closest_lambda_ind)
        last_steps.clear()

if state != State.OK:
    print(state)
    print('score:', score)
    exit(0)

# going outside
way = maze.astar(maze.R, maze.exit)
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
    state, new_score = maze.move_to(wnext)
    score = score - 1 + new_score
    if state != State.OK:
        break

    maze.update()

    try:
        wnext = next(way)
    except StopIteration:
        state = State.WIN

if state != State.OK:
    print(state)
    print('score:', score)
    exit(0)
