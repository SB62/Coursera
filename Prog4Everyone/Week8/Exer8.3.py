fhand = open('mbox-short-mod.txt')
count = 0
for line in fhand:
    words = line.split()
    #print 'Debug:', words
    if not (len(words) > 3 and words[0] == 'From') : continue
    
    print words[2]
