
import random

# method to generate an individual
# generates a binary number as an array of the given size
def gen_individual(size=6):
    return [random.randint(0,1) for i in range(size)]

# generates a population by generating a given number of individuals ( SIZE MUST BE EVEN )
def gen_initial_pop(size=12):
    pop = []
    for _ in range(10):
        pop.append([gen_individual(),0])
    
    return pop

# a method to simulate mutation
# there will be a small chance to mutate
# if mutate return 0 there will not be a mutation, if 1 there will be
def mutate(r):
    return random.choices([False,True], weights=[100-r,r])[0]

# method to evaluate an organism
def evaluate(ind, target):
    score = 0
    dna = ind[0]
    # give one point for each different bit to the target
    for i in range(len(target)):
        if dna[i] != target[i]:
            score += 1
    
    return score

# method to evaluate the entire population
def full_eval(pop, target):
    for organism in pop:
        organism[1] = evaluate(organism, target)

# method to simulate crossing over between two parent organisms
def cross(p1, p2):
    # find the half way point
    half = len(p1[0]) // 2
    # simulate crossing over by taking the first half of p1 and the second half of p2
    child = [p1[0][:half] + p2[0][half:], 0]
    
    # simulate chance of mutation
    if mutate(2):
        pos = random.randint(0,len(child[0])-1)
        child[0][pos] = 0 if child[0][pos] == 1 else 1
        
    return child

# method to simulate repopulation
def repopulate(pop, target):
    c1 = None
    c2 = None
    # choose every even member of the population
    for i in range(2,len(pop),2):
        # if the index is less than the max index of the population array
        if i < len(pop):
            # cross the organism with its immediate neighbors
            c1 = cross(pop[i],pop[i-1])
            c2 = cross(pop[i],pop[i+1])
            # evaluate the new children
            c1[1] = evaluate(c1, target)
            c2[1] = evaluate(c2, target)
            # add the new children to the population
            pop.append(c1)
            pop.append(c2)
        # if the index is equal to the max index of the population array
        else:
            # cross the organism with its left neighbor and the first organism in the population array
            c1 = cross(pop[i],pop[i-1])
            c2 = cross(pop[i],pop[0])
            # evaluate the new children
            c1[1] = evaluate(c1, target)
            c2[1] = evaluate(c2, target)
            # add the new children to the population
            pop.append(c1)
            pop.append(c2)

# generate a target genome
target = [random.randint(0,1) for i in range(6)]
print(f"Target: {target}\n")
# generate a population
pop = gen_initial_pop()

# evaluate all initial organisms in the population
full_eval(pop, target)
print(f"Initial Population: \n{pop} \n")

for _ in range(100):
    # choose the best six and cross over with immediate neighbors
    pop = sorted(pop, key=lambda p: p[1])[:6]
    # cross over the survivors
    repopulate(pop, target)

# sort the population array by their scores to find the organism closest to the target organism
pop = sorted(pop, key=lambda p: p[1])
print(f"Final Population: \n{pop}\n")
selected = min(pop, key=lambda p: p[1])
print(f"Best Fit: {selected}")