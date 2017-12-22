# Entre 7_9_9 x64.ism
fhand = open('Entre 7_9_9 x64.ism')
print(type(fhand))
count = 0
for line in fhand:
    count = count + 1

print('Line Count:', count)