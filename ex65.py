text = "X-DSPAM-Confidence:    0.8475"
startpos = text.find('0')
number = float(text[startpos:])
print(number)