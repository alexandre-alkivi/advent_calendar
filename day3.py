def readfile(path):
	data = []
	with open(path, 'r') as content:
		for line in content.readlines():
			data.append(line.strip())
	return data

def rowMatching(bag, position):
	while (position[0] < position[2]/2 and bag[position[0]] != bag[position[1]]):
		position[0] +=1
	if position[0] == position[2]/2:
		position[0] = 0
		position[1] +=1
		if position[1] == position[2]:
			print("overflow")
			return [0]
		return rowMatching(bag,position) 
	else:
		return (position[0])

def rowMatching2(bag1, bag2, bag3, position1, position2, position3):
	while (position1 < len(bag1) and bag1[position1] != bag2[position2]):
		position1 += 1
	if position1 == len(bag1):
		position1 = 0
		position2 +=1
		if position2 == len(bag2):
			print("overflow")
			return [0,0,0]
		return rowMatching2(bag1, bag2, bag3, position1, position2, position3)
	else:
		while (position3 < len(bag3) and bag2[position2] != bag3[position3]):
			position3 +=1
		if position3 == len(bag3):
			position1 = 0
			position2 +=1
			position3 = 0
			if position2 == len(bag2):
				print("overflow")
				return [0,0,0]
			return rowMatching2(bag1, bag2, bag3, position1, position2, position3)
		else:
			return position1

def getMatchingItem(bag):
	length = len(bag)/2
	position = [0,int(len(bag)/2),len(bag)]
	return rowMatching(bag,position)


def itemValue(item):
	if item.isupper():
		return ord(item)-38
	else:
		return ord(item)-96

def day3Part1(data):
	total = 0
	for bag in data:
		total += itemValue(bag[getMatchingItem(bag)])
	print(total)

def day3Part2(data):
	count = 0
	total = 0
	while count < len(data):
		group = []
		for i in range (0,3):
			group.append(data[count])
			count += 1
		# print(group)
		position = rowMatching2(group[0], group[1], group[2], 0,0,0)
		total += itemValue(group[0][position])
	print (total)

day3Part1(readfile("./day3.txt"))
day3Part2(readfile("./day3.txt"))

