from collections import deque

initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

def is_valid (state):
    missionaries_left, cannibals_left, boat_location = state
    
    if (
        missionaries_left < 0
        or cannibals_left < 0
        or missionaries_left > 3
        or cannibals_left > 3
    ):
        return False
    if (
        (missionaries_left < cannibals_left and missionaries_left > 0)
        or (3 - missionaries_left < 3 - cannibals_left and 3 - missionaries_left > 0)
    ):
        return False
    
    return True

def get_next_states(state):
    states = []
    missionaries_left, cannibals_left, boat_location = state
    passengers = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    
    for m, c in passengers:
        new_missionaries_left = missionaries_left - m * boat_location
        new_cannibals_left = cannibals_left - c * boat_location
        new_boat_location = 1 - boat_location
        
        new_state = (new_missionaries_left, new_cannibals_left, new_boat_location)
        if is_valid (new_state):
            states.append(new_state)
    return states

def solve():
    visited = set()
    queue = deque([(initial_state, [])])
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [current_state]
        
        visited.add(current_state)
        next_states = get_next_states(current_state)
        
        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
    return None

solution = solve()

if solution:
    print("Solution: ")
    for i, state in enumerate(solution):
        print (f"Step {i + 1}: {state}")
else:
    print("No solution found")
