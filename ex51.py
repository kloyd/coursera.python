total = 0.0
count = 0
while True :
    numberin = input("Enter a number: ")
    if numberin == "done":
    	break
    try:
    	thenumber = float(numberin)
    except:
    	print("Invalid Input")
    	continue
    # add up and count
    total = total + thenumber
    count = count + 1

print(total, count, total / count)
