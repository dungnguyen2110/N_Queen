import time
from random import randint

# Generate chess board N x N
def generate_random_board(N):
    return [randint(0, N-1) for _ in range(N)]

# Print board
def print_board(state):
    for row in state:
            print(" ".join("Q" if col == row else "." for col in range(N)))
            
def compareStates(state1, state2):
    return state1 == state2

# Calc the number of conflicts between queens
def calculate_attacks(board):
    N = len(board)
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def getNeighbour(state):
    opState = state[:]
    opObjective = calculate_attacks(opState)

    for i in range(N):
        for j in range(N):
            if state[i] != j:
                tempState = state[:]
                tempState[i] = j
                tempObjective = calculate_attacks(tempState)
                if tempObjective <= opObjective:
                    opObjective = tempObjective
                    opState = tempState

    state[:] = opState

# Solve the N-queens problem using Hill Climbing
def hill_climbing(state, time_max):
    start_time = time.time()
    
    while True:
        time_run = time.time() - start_time
        if time_run > time_max:
            return None, time_max
        
        
        currentState = state[:]
        currentObjective = calculate_attacks(currentState)
        getNeighbour(state)

        if compareStates(currentState, state):
            return  state, time_run
        elif currentObjective == calculate_attacks(state):
            # Jump to a random neighbor to escape local optima
            state[randint(0, N - 1)] =randint(0, N - 1)



N = int(input("Input N for N-queens: "))
time_max = int(input("Input limit time: "))

# Initialize state for board
state = generate_random_board(N)

solution, time_run = hill_climbing(state, time_max)


if solution != None:
    if calculate_attacks(solution) == 0:
        print("Time run: ", time_run)
        
        print("Solution")
        print_board(solution)
    else:
        print("No results were found after running the algorithm")
        print(calculate_attacks(solution))
else:
    print("No results were found after running the algorithm")
