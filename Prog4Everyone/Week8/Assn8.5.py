fname = raw_input('Enter File Name: ')

try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

lst = list()
count = 0

for line in fhand:
    sline = line.split()
    if not (len(sline) > 3 and sline[0] == 'From') : continue
    count = count+1
    print sline[1]

print 'There were', count, "lines in the file with From as the first word"
