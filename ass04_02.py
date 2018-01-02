import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL:')
inpcount = input('Enter count:')
inppos = input('Enter position:')
maxcount = int(inpcount)
pos = int(inppos)

count = 0
# include first retrieval in the count, to save repeating the fetch sequence
while count <= maxcount:
	print('Retrieving:', url)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	position = 1


# Retrieve all of the anchor tags, skip until reaching pos
	tags = soup('a')
	for tag in tags:
		if position < pos:
			position = position + 1
			#print('skipping ', tag['href'])
			continue
		else:
			url = tag['href']
			break

	count = count + 1

# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html 
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah 
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Annaliesse.html 
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: K