

import random
import matplotlib.pyplot as plt

# generate a random binary solution
def generate_solution(size=5):
    solution = []
    # choose either 1 or 0 for each position
    for _ in range(size):
        solution.append(random.randint(0,1))
    return solution

# method to mutate a solution
def mutate(solution):
    # choose a random position to change
    pos = random.randint(0,len(solution)-1)
    solution[pos] = 0 if solution[pos] == 1 else 1

# method to evaluate a solution
def evaluate(solution, target):
    score = 0
    for i in range(len(solution)):
        score += abs(solution[i] - target[i])
    return score

target = [random.randint(0,1) for i in range(16)]

times = []
for i in range(25):
    print("Run: " + str(i+1))
    # generate a starting solution
    best = generate_solution(16)
    # evaluate the starting solution
    best_score = evaluate(best, target)
    iterations = 0
    print(target)
    # beginning of the algorithm
    while True:
        iterations +=1
        # print the current best solution and score
        print("Best Score: " + str(best_score))
        print("Solution: ", end=" ")
        print(best, end=" Iterations: " + str(iterations) + "\n")
        
        # if the target solution is found break out of the loop
        if best_score == 0:
            break
            
        # mutate the solution
        next_solution = best.copy()
        mutate(next_solution)
        # evaluate the new solution
        new_score = evaluate(next_solution, target)
        
        # if the new solution score is better than the current best, replace the current best
        if new_score < best_score:
            best = next_solution.copy()
            best_score = new_score
    
    times.append(iterations)

# graph to show the number of iterations each run took
x = [i for i in range(1,26)]
plt.xlabel("Run")
plt.ylabel("Iterations")
plt.plot(x,times)
plt.show()