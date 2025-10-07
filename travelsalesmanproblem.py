import random

MAX_TRIALS = 100

tsp = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

cities = len(tsp)

def Value(state):
    total = 0
    for i in range(len(state)):
        total += tsp[state[i]][state[(i + 1) % cities]]
    return total

def get_neighbor(state):
    neighbor = state[:]
    i, j = random.sample(range(1, cities), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def hill_climbing(state):
    current = state
    current_value = Value(current)
    for _ in range(MAX_TRIALS):
        neighbor = get_neighbor(current)
        neighbor_value = Value(neighbor)
        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value
    return current

best_state = []
best_dist = float('inf')

for _ in range(20):
    state = list(range(cities))
    state_rest = state[1:]
    random.shuffle(state_rest)
    state = [0] + state_rest
    state = hill_climbing(state)
    v = Value(state)
    if best_dist > v:
        best_dist = v
        best_state = state

print(best_state, best_dist)
