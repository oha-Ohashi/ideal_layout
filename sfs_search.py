import sbs_io as io
import sbs_evaluate as ev
import copy
import random, math
import sys, time
random.seed(1)

def nth_layout(N):
	abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	S = len(abc)
	r = [""] * (S+1)
	for i in range(1, S+1):
		q, mod = divmod(N, i)
		r[i] = mod
		N = q
	B = []
	for i in reversed(list(range(1, S+1))):
		k = r[i]
		B.append(abc[k])
		abc.remove(abc[k])
	#B = "".join(B)
	return B

def ga(ms):								# roulette wheel selection
	population_size = 50
	n_generation = 100
	i_all = list(range(population_size))
	values = [random.randint(0, math.factorial(26 - 1)) for _ in range(population_size)]
	for i_gen in range(n_generation):
		costs, fitnesses = get_costs_fitnesses(values, ms)
		print(i_gen, "th gen, ",end=" ")
		print("variety: ", len(set(fitnesses)),end=" ")
		print("min cost ", min(costs))
		#print(fitnesses)
		#showfitnesses(fitnesses)
		roulette_border = 0
		borders = []
		for i in range(population_size):
			roulette_border += fitnesses[i] / sum(fitnesses)
			borders.append(roulette_border)

		i_survivers = []
		for i in range(population_size):
			i_survivers.append(pick_roulette(random.random(), borders))

		new_values = []
		for i in range(population_size):
			child = 0
			if random.random() < 0.8:
				i_parents = random.sample(i_survivers, 2)
				'''i_parents = [
					pick_roulette(random.random(), borders),
					pick_roulette(random.random(), borders)
				]'''
				child = two_point_crossover(values[i_parents[0]], values[i_parents[1]])
				pass
			else:
				child = values[i_survivers[random.sample(i_survivers, 1)[0]]]
				pass
			if random.random() < 0.01:
				child = mutation(child, 1)
			new_values.append(child)
		values = new_values

def ga2(ms):								# roulette wheel selection
	population_size = 50
	n_generation = 100
	i_all = list(range(population_size))
	# population initialization
	values = [random.randint(0, math.factorial(26 - 1)) for _ in range(population_size)]

	for i_gen in range(n_generation):
		costs = list(map(
			lambda v: ev.evaluate(ms.mizuni_modosu(nth_layout(v))).cost_sum, 
			values))
		print(i_gen, "th gen,",end=" ")
		print(", diversity:", len(set(values)), end=" ")
		print(", min_cost:", min(costs), end=" ")
		print(", mean_cost:", sum(costs)/len(costs))

		new_values = []
		elites = sorted(costs)[0:1]
		#elites = []
		for el in elites:
			new_values.append(values[costs.index(el)])

		survivers = []
		for i in range(population_size):
			#survivers.append(roulette_wheel_selection_reciprocal(values, costs))
			#survivers.append(tounament_selection(values, costs, 3))
			survivers.append(rank_selection(values, costs))

		while(len(new_values) < population_size):
			child = 0
			if random.random() < 1.0:
				parents = random.sample(survivers, 2)
				child = uniform_crossover(parents[0], parents[1])
				pass
			else:
				child = random.sample(survivers, 1)[0]
				pass
			if random.random() < 0.01:
				child = mutation(child, 1)
			new_values.append(child)
		values = new_values

def get_costs_fitnesses(values, ms):
	#print(values)
	costs = list(map(
		lambda value: ev.evaluate(ms.mizuni_modosu(nth_layout(value))).cost_sum,
		#lambda value: ev.evaluate(ms.mizuni_modosu(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))).cost_sum,
		values
	))
	#print(costs)
	fitnesses = list(map(lambda cost: max(costs) - cost, costs))
	#print(fitnesses)
	return costs, fitnesses

def showfitnesses(fitnesses):
	for i in range(len(fitnesses)):
		print(fitnesses[i])
	for i in range(len(fitnesses)):
		print("\033[1A",end="")


def pick_roulette(rand, borders):
	res = 0
	while(rand > borders[res]):
		res += 1
	return res

def roulette_wheel_selection_reciprocal(values, costs):
	min_cost = min(costs)
	#costs = list(map(lambda x: x - min_cost + 2000, costs))
	costs = list(map(lambda x: x - 15000, costs))
	current_border = 0
	borders = [0]
	ps = [0] * len(values)
	for i in range(len(values)):
		ps[i] = 1 / (costs[i] ** 1)
	ps = list(map(lambda x: x/sum(ps), ps))
	for p in ps:
		borders.append(borders[-1] + p)
	#print("eob:", borders[-1])
	rnd = random.random()
	#print("rnd:", rnd)
	i_selected = 0
	while True:
		if rnd < borders[i_selected +1]:
			return values[i_selected]
		i_selected += 1

def tounament_selection(values, costs, n_cands):
	costs_cands = []
	for i in range(n_cands):
		costs_cands.append(costs[random.randint(0, len(costs) - 1)])
	min_cost = min(costs_cands)
	return values[costs.index(min_cost)]

def rank_selection(values, costs):
	sorted_costs = sorted(costs)
	sorted_costs.reverse()
	roulette_borders = [0]
	ranks = list(range(1, len(costs) + 1))
	for r in ranks:
		roulette_borders.append(roulette_borders[-1] + (r / sum(ranks)))
	rnd = random.random()
	i_selected = 0
	while True:
		if rnd < roulette_borders[i_selected +1]:
			return values[costs.index(sorted_costs[i_selected])]
		i_selected += 1

def crossover(parent1, parent2):
	return parent1

def mutate(chromosome):
	return chromosome

def uniform_crossover(parent1, parent2):
	res = 0
	mask = random.randint(0, math.factorial(26) - 1)
	for i in range(89):
		if 0b1 << i & mask:
			res = res | (0b1 << i & parent1)
		else:
			res = res | (0b1 << i & parent2)
	return res

def two_point_crossover(parent1, parent2):
	res = 0
	points = sorted([random.randint(0, 89 - 1), random.randint(0, 89 - 1)])
	#print(points)
	for i in range(89):
		if i < points[0]:
			res = res | (0b1 << i & parent1)
		elif i < points[1]:
			res = res | (0b1 << i & parent2)
		else: 
			res = res | (0b1 << i & parent1)
	return res

def mutation(child, n_flip):
	for i in range(n_flip):
		x = random.randint(0, 89 - 1)
		child = child ^ (0b1 << x)
	return child


if __name__ == '__main__':
	time_start = time.time()

	mx = math.factorial(26)
	
	ms = io.MojiretsuSousa('config.txt')

	ga2(ms)

	print(time.time() - time_start)

	'''
	for j in range(10):
		for i in range(5):
			print(j)
		for i in range(5):
			print("\033[1A",end="")
		time.sleep(0.5)
	for i in range(5):
		print()
	'''
		#print("\033[1A",end="")
		#print(random.randint(0, 5)) 0,1,2,3,4,5
	#for i in range(30):
		#print(random.random())