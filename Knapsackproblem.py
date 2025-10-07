import random
from math import exp

Objects = {'A': (10, 2), 'B': (6, 3), 'C': (4, 8),
           'D': (8, 5), 'E': (9, 5), 'F': (7, 6)}
C = 15
Items = list(Objects.keys())
nObjects = len(Objects)

def Value(state):
    total_weight = 0
    total_value = 0
    for i in range(nObjects):
        if state[i] == 1:
            w, v = Objects[Items[i]]
            total_weight += w
            total_value += v
    if total_weight > C:
        return -1
    return total_value

def get_neighbor(state):
    neighbor = state[:]
    i = random.randrange(nObjects)
    neighbor[i] = 1 - neighbor[i]
    return neighbor

def simulated_annealing(max_iterations=1000, initial_temp=100, alpha=0.95):
    current = [random.randrange(2) for _ in range(nObjects)]
    best = current
    current_value = Value(current)
    best_value = current_value
    T = initial_temp
    
    for _ in range(max_iterations):
        neighbor = get_neighbor(current)
        neighbor_value = Value(neighbor)
        delta = neighbor_value - current_value
        if delta > 0 or random.random() < exp(delta / T):
            current = neighbor
            current_value = neighbor_value
            if current_value > best_value:
                best = current
                best_value = current_value
        T *= alpha
        if T < 0.001:
            break
    return best, best_value

best_overall_state = None
best_overall_value = -1
restarts = 20

for _ in range(restarts):
    state, val = simulated_annealing()
    if val > best_overall_value:
        best_overall_state = state
        best_overall_value = val

print("Best state found:", best_overall_state)
print("Best value found:", best_overall_value)
