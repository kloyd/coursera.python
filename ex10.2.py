name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	if len(words) == 0 : continue
	if words[0] != 'From': continue
	#print(words)

	word = words[5]
	digits = word.split(':')
	hours = digits[0]
	#print(digits)
	if hours not in counts:
		counts[hours] = 1
	else:
		counts[hours] = counts[hours] + 1

lst = list()
for key, val in list(counts.items()):
	lst.append((key, val))

lst.sort()

for key, val in lst:
	print(key, val)

