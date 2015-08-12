lst = list()

while (True):
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    if inp == 'Done': break
    inp = float(inp)
    lst.append(inp)

    #print "Debug:", lst
print max(lst)
print min (lst)
