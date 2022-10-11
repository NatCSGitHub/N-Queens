#Natasha Needham
#CS441 Winter 2021
#Python 8 Queens Program
import random

def random_chromosome(size): #making random chromosomes 
	return [ random.randint(1, 8) for _ in range(8) ]

def fitness(chromosome):
	horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2
	diagonal_collisions = 0

	n = len(chromosome)
	left_diagonal = [0] * 2*n
	right_diagonal = [0] * 2*n
	for i in range(n):
        	left_diagonal[i + chromosome[i] - 1] += 1
        	right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

	for i in range(2*n-1):
        	counter = 0
        	if left_diagonal[i] > 1:
            		counter += left_diagonal[i]-1
        	if right_diagonal[i] > 1:
            		counter += right_diagonal[i]-1
        	diagonal_collisions += counter / (n-abs(i-n+1))
    
	return int(maxFitness - (horizontal_collisions + diagonal_collisions)) #28-(2+3)=23

def probability(chromosome, fitness):
	return fitness(chromosome) / maxFitness

def random_pick(population, probabilities):
	population_prob = zip(population, probabilities)
	total = sum(w for c, w in population_prob)
	r = random.uniform(0, total)
	upto = 0
	for c, w in zip(population, probabilities):
		if upto + w >= r:
			return c
		upto += w
	assert False, "Error"
        
def crossover(x, y):
	n = len(x)
	c = random.randint(0, n - 1)
	return x[0:c] + y[c:n]

def mutate(x):  #randomly changing the value of a random index of a chromosome
	n = len(x)
	c = random.randint(0, n - 1)
	m = random.randint(1, n)
	x[c] = m
	return x

def genetic_alg(population, fitness):
	mutation_probability = 0.03
	new_population = []
	probabilities = [probability(n, fitness) for n in population]
	for i in range(len(population)):
		x = random_pick(population, probabilities) #best chromosome 1
		y = random_pick(population, probabilities) #best chromosome 2
		child = crossover(x, y) #creating two new chromosomes from the best 2 chromosomes
		if random.random() < mutation_probability:
			child = mutate(child)
		print_chromosome(child)
		new_population.append(child)
		if fitness(child) == maxFitness:
			break
	return new_population

def print_chromosome(chrom):
	print("Chromosome = {},  Fitness = {}".format(str(chrom), fitness(chrom)))

if __name__ == "__main__":
	maxFitness = (8*(8-1))/2  # 8*7/2 = 28
	#population = 100 gives a decent fitness, typically around 25 or so; increasing to 200 only puts fitness at around 27,
		#so not much of an improvement; finding a solution with 28 fitness typically takes upwards of 1000 generations
	population = [random_chromosome(8) for _ in range(100)]
	
	total = 0
	average = 0 
	generation = 1

	#the following line used for finding a solution with max fitness
	#while not maxFitness in [fitness(chrom) for chrom in population]:
	#chose arbitrary number for stopping condition
	while generation <= 20 : 
		print("=== Generation {} ===".format(generation))
		population = genetic_alg(population, fitness)
		print("")
		print("Highest Fitness Reached This Generation = {}".format(max([fitness(n) for n in population])))
		total += max([fitness(n) for n in population])
		average = total/generation
		print()
		print(f"Average maximum fitness: {average:0.4f}")
		generation += 1
	chrom_out = []
	print("Solved in Generation {}".format(generation-1))
	for chrom in population:
		#if fitness(chrom) == maxFitness:
		print("");
		print("One of the solutions: ")
		chrom_out = chrom
		print_chromosome(chrom)


	print()     
	print("The final board:")     
	board = []

	for x in range(8):
		board.append(["x"] * 8)
        
	for i in range(8):
		board[8-chrom_out[i]][i]="Q"
            

	def print_board(board):
		for row in board:
			print (" ".join(row))
	print()
	print_board(board)
