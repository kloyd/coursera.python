fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

fromlist = dict()

for lines in fh:
    if 'From ' in lines:
        words = lines.split()
        fromlist[words[1]] = fromlist.get(words[1], 0) + 1
       
largestemail = None
largestcount = None
for key,v  in fromlist.items():
    if largestcount is None:
        largestcount = v
        largestemail = key
    elif largestcount < v:
        largestcount = v
        largestemail = key

print(largestemail, largestcount)

