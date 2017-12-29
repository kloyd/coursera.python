import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
count = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
	num = int(tag.contents[0])
	sum = sum + num
	count = count + 1

print('Count', count)
print('Sum', sum)


# http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# http://py4e-data.dr-chuck.net/comments_58300.html (Sum ends with 55)
