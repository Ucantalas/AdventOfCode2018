frequency = int(0)
print "Test"
file_object = open("input.txt", 'r')

for line in file_object:
	frequency += int(line)

print frequency
