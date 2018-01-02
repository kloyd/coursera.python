#assignment 05_01.py
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
hand = urllib.request.urlopen(url)
data = hand.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = 0
print('Count:', len(counts))
for item in counts:
	count = int(item.text)
	sum = sum + count

print('Sum:', sum)


# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_58302.xml (Sum ends with 58)

