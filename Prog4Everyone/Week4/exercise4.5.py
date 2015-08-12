def computegrade(x):
    if x <= 1.0 and x >= .9:
        return "A"
    elif x < .9 and x >= .8:
        return "B"
    elif x < .8 and x >= .7:
        return "C"
    elif x < .7 and x >= .6:
        return "D"
    else:
        return "F"

g = raw_input("Enter Score:")
try:
    g = float(g)
except:
    g = -1

if g >= 0:
    grade = computegrade(g)
    print grade
else:
    print "Bad Score"
