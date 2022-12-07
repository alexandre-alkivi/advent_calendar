import re

def readfile(path):
	data = []
	with open(path, 'r') as content:
		for line in content.readlines():
			data.append(line.strip())
	return data


def isContained(area):
	if area[0] >= area[2] and area[1] <= area[3]:
		return True
	elif area[2] >= area[0] and area[3] <= area[1]:
		return True
	return False

def isOverlaping(area):
	if area[0] >= area[2] and area[0] <= area[3]:
		return True
	elif area[2] >= area[0] and area[2] <= area[1]:
		return True
	return False

def day4(data):
	area = []
	contained = 0
	overlap = 0

	for line in data:
		p = '[\d]+'
		if re.search(p, line) is not None:
			for match in re.finditer(p, line):
				area.append(int(match[0]))
		if isContained(area):
			contained +=1
		if isOverlaping(area):
			overlap +=1
		area = []
	print (contained, " contained")
	print (overlap, " overlaps")
	

day4(readfile("./day4.txt"))
