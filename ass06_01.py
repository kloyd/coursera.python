import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
sum = 0
count = 0

try:
	js = json.loads(data)
except:
	js = None

for item in js['comments']:
	val = int(item['count'])
	sum = sum + val
	count = count + 1

print('Count:', count)
print('Sum:', sum)

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_58303.json (Sum ends with 97)