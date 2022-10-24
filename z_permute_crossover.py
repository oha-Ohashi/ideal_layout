import random
p1 = list("987654321")
p2 = list("246813579")

def partially_mapped_crossover(p1, p2):
	child = [" " for _ in range(len(p1))]
	border = sorted([random.randint(0, len(p1)-1), random.randint(0, len(p1)-1)])
	mapindex = list(range(border[0], border[1] + 1))
	for i in mapindex:
		child[i] = p2[i]
	for i in range(len(p1)):
		if not i in mapindex and not p1[i] in child:
			child[i] = p1[i]
	for i in range(len(p1)):
		if not p1[i] in child:
			child[child.index(" ")] = p1[i]
	return child

print(p1)
print(p2)
print(partially_mapped_crossover(p1, p2))
print(partially_mapped_crossover(p1, p2))
for i in range(1000):
	partially_mapped_crossover(p1, p2)

'''
for i in range(20):
	a = sorted([random.randint(8, 10), random.randint(8, 10)])
	print(list(range(a[0], a[1] + 1)))
'''