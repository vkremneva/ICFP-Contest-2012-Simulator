from Algorithm import*
from copy import deepcopy
from collections import defaultdict

amount_of_steps_to_remember = 3
critical_count_visits = 10

maze = Algorithm()
maze.read('maps\\contest9.map')

# initial values
score = 0
current = maze.R
state = State.OK
last_steps = []
unreachable_lambdas = []
count_visits = defaultdict(int)
possible_lambdas = deepcopy(maze.lambdas)

# gather lambdas
while (len(maze.lambdas) != 0) and (len(possible_lambdas) != 0):
    closest_lambda_ind = min(possible_lambdas, key=lambda x: maze.heuristic_cost_estimate(current, x))

    way = maze.astar(current, closest_lambda_ind)
    wnext = ()

    if way is None:
        unreachable_lambdas.append(closest_lambda_ind)
        if closest_lambda_ind in possible_lambdas:
            possible_lambdas.remove(closest_lambda_ind)
        continue

    if type(way) == list:
        state = State.WIN
        break
    else:
        try:
            next(way)
            wnext = next(way)
        except StopIteration:
            state = State.WIN
            break

    if count_visits[wnext] == 10:
        state = State.WIN
        break

    state, new_score = maze.move_to(wnext)
    count_visits[wnext] += 1
    if new_score == 25:
        for l in possible_lambdas:
            if not(l in maze.lambdas):
                possible_lambdas.remove(l)
                break
        if (len(unreachable_lambdas) != 0) and (len(possible_lambdas) == 0):
            possible_lambdas.append(unreachable_lambdas.pop())

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
            if closest_lambda_ind in possible_lambdas:
                possible_lambdas.remove(closest_lambda_ind)
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
