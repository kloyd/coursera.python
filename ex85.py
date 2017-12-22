fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for lines in fh:
    if 'From' in lines:
        if 'From:' in lines:
            continue
        words = lines.split()
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
