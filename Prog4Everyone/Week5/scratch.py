#Variables
largest = None
smallest = None

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
#Smallest and largest storage
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num
#Results
print "Maximum is", largest
print "Minimum is", smallest
