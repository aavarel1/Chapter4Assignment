import random
MAX_TRIALS = 100
tsp = [[0, 400, 500, 300],
[400, 0, 300, 500],
[500, 300, 0, 400],
[300, 500, 400, 0]
]
cities = len(tsp)
def Value(state):
# write your code here
def get_neighbor(state):
# write your code here
def hill_climbing(state):
# write your code here
best_state = []
best_dist = 100000
for k in range(20):
state = list(range(cities))
random.shuffle(state)
state = hill_climbing(state)
v = Value(state)
if best_dist > v:
best_dist = v
best_state = state
print(best_state, best_dist)
