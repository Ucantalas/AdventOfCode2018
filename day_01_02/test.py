frequency = int(0)
listOfFrequencies = list([0])
print "Day 1 Part 2: Find first instance of frequency appearing twice."

exitCount = 0

while exitCount == 0:
	file_object = open("input.txt", 'r')
	for line in file_object:
		frequency += int(line)
		listOfFrequencies.append(frequency)
		if listOfFrequencies.count(frequency) > 1:
			print "Found twice! ", frequency 
			exitCount = 1
		

print frequency
print listOfFrequencies