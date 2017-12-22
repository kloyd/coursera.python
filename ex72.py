# Use the file name mbox-short.txt as the file name
count = 0
total = 0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    workline = line.rstrip()
    pos = workline.find(' ')
    total = total + float(workline[pos:])
    count = count + 1
print('Average spam confidence:', total / count)


# Average spam confidence: 0.750718518519