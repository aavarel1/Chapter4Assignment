def get_neighbor(state):
    neighbors = []
    for i in range(len(state)):
        if state[i] % 2 == 0:
        neighbors.append(i)
    return neighbors
