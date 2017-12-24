txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
	t.append((len(word), word))   # The () around value, key creates a tuple.
	# the tuple is appended to the list.

print(t)

t.sort(reverse=True) #since tuples are comparable, we can sort the list. (4, 'fred') < (4, 'yang')
#                      compare 4 to 4, equal, compare 'fred' to 'yang' - less than. ;)

res = list()
for length, word in t:
	res.append(word)

print(res)
