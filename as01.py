import re
sum = 0
hand = open('regex_sum_58298.txt')
for line in hand:
	numstrs = re.findall('[0-9]+', line)
	if len(numstrs) > 0:
		print(numstrs)
		for num in numstrs:
			val = int(num)
			sum = sum + val

print(sum)