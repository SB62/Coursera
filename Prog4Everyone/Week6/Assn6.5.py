str = 'X-DSPAM-Confidence: 0.8475'

start = str.find(':')
#print start
#print str[start:]
data = float(str[start+1:])
print data
#print type(data)
