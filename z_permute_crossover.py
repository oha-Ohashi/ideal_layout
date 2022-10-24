p1 = list("987654321")
p2 = list("246813579")

def cross(p1, p2):
	print(p1)
	print(p2)
	border = [2, 8]
	child = [" " for _ in range(len(p1))]
	mapindex = list(range(border[0], border[1]))
	for i in mapindex:
		child[i] = p2[i]
	print(child)
	for i in range(len(p1)):
		if not p1[i] in child and not i in mapindex:
			child[i] = p1[i]
	print(child)

	return child

cross(p1, p2)
#print(cross(p1, p2))