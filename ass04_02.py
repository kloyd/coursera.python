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

