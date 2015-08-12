fname = raw_input('Enter the file name: ')
count = 0
total = 0
# if fname == 'na na boo boo':
#     print "NA NA BOO BOO TO YOU - You have just been punk'd!"
#     exit()
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence"):
        continue

    start = line.find(':')
    num = float(line[start+1:])
    # print 'Start:', start
    # print 'Num:', num
    count = count + 1
    total = num + total
    # print 'Total:', total
# print 'Count:', count
print 'Average spam confidence:', (total/count)
fhand.close
