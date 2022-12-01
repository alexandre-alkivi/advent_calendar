def day1():
	file = open('data', 'r')
	content = file.readlines()
	length = len(content)
	elf = 0
	max = [0,0,0]
	line = 0
	while line < length:
		while (line < length and content[line] != "\n"):
			elf = elf + int(content[line])
			line = line + 1
		# print ("elfe : " + str(elf) + "\nmeilleur : " + str(max))
		if (max[0] < elf):
			print (max)
			if (max[1] < elf):
				if (max[2] < elf):
					max[0] = max[1]
					max[1] = max[2]
					max[2] = elf
				else:
					max[0] = max[1]
					max[1] = elf
			else:
				max[0] = elf
		elf = 0
		line = line + 1
	print (max)
	print (max[0] + max[1] + max[2])
	file.close()
day1()
