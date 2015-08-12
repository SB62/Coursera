#Variables
count = 0
total = 0

while True:
    inp = raw_input("Enter a Number: ")
#Loop
    if inp == "done":
        break
    if inp == "Done":
        break
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
#The work
    count = count + 1
    total = total + num
#    print num, total, count
print total, count, total/count
