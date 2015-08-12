hrs = raw_input("Enter Hours:")
rte = raw_input("Enter Pay Rate:")
try:
    hrs = float(hrs)
    rte = float(rte)
except:
    hrs = -1
if hrs > 0:
    if hrs <= 40:
        x = hrs
        gross = (x * rte)
    
    elif hrs > 40:
        y = hrs - 40
        x = 40
        gross = (x * rte) + (y * (1.5 * rte))
    print gross 

else:
    print "Please use numeric value"