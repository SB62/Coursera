#Define computation
def computepay(h,r):
    if h <= 40:
        gross = (h * r)
    elif h > 40:
        y = h - 40
        x = 40
        gross = (x * r) + (y * (1.5 * r))
    return gross
#Prompt for user input    
hrs = raw_input("Enter Hours:")
rte = raw_input("Enter Pay Rate:")
#Check to see if the input is numeric
try:
    hrs = float(hrs)
    rte = float(rte)
#If not numeric, then  set up for conditional statement to fail out
except:
    hrs = -1
#Run Conditional statement to test, run program if pass
if hrs > 0:
    pay = computepay(hrs,rte)
    print pay 

else:
    print "Please use numeric value"
