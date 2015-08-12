fname = raw_input('Enter File Name: ')

try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

lst = list()

for line in fhand:
    wrdlst = line.split()

    for word in wrdlst:
#        print 'word is:', word
        if word not in lst:
            lst.append(word)
#            print "List contains:", lst
#print lst
lst.sort()
print lst
