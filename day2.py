def readfile(path):
	data = []
	with open(path, 'r') as content:
		for line in content.readlines():
			data.append(line.strip())
	return data

def gameResult1(battle):
	count = 0
	match battle[2]:
		case "X":
			count = 1
			match battle[0]:
				case "A":
					return count + 3
				case "B":
					return count
				case "C":
					return count + 6
		case "Y":
			count = 2
			match battle[0]:
				case "A":
					return count + 6
				case "B":
					return count + 3
				case "C":
					return count
		case "Z":
			count = 3
			match battle[0]:
				case "A":
					return count
				case "B":
					return count + 6
				case "C":
					return count + 3
	return 0

def gameResult2(battle):
	count = 0
	match battle[2]:
		case "X": # lose
			match battle[0]:
				case "A":
					return 3
				case "B":
					return 1
				case "C":
					return 2
		case "Y": # draw
			count = 3
			match battle[0]:
				case "A":
					return count + 1
				case "B":
					return count + 2
				case "C":
					return count + 3
		case "Z": # win
			count = 6
			match battle[0]:
				case "A":
					return count + 2
				case "B":
					return count + 3
				case "C":
					return count + 1
	return 0

def day2(data):
	total = 0
	for battle in data:
		total += gameResult1(battle)
	print(total)
	total = 0
	for battle in data:
		total += gameResult2(battle)
	print(total)


day2(readfile("./day2.txt"))
