#List auto generated
#lst = list(range(10))

#User generated list
lst = list()
while (True):
    inp = raw_input("Enter something:")
    if inp == 'done': break
    lst.append(inp)

#function to remove first and last latters
def chop(t):
    del t[0]
    del t[-1]

#function to make return just middle of the list
def middle(t):
    return t[1:-1]

mid = middle(lst)
chop(lst)

print mid
print lst
