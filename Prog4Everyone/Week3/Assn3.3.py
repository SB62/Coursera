x = raw_input("Enter Score:")
try :
    x = float(x)
except :
    print 'Please enter a numeric value between 1.0 and 0'
    quit()
if x >= 0 and x <= 1 :
    if x <= 1.0 and x >= 0.9:
        print "A"
    elif x < .9 and x >= .8:
        print "B"
    elif x < .8 and x >= .7:
        print "C"
    elif x < .7 and x >= .6:
        print "D"
    else: 
        print "F"
else :
    print 'Please enter a number between 1.0 and 0'