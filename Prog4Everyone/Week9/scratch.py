def words_count():
    wordstore = dict()
    fhand = open(inp)

    for line in fhand:
        for words in line.split():
            wordstore[words] = len(words)
    fhand.close()
    return wordstore

inp = raw_input("What File are you searching? ")
search = raw_input("What word are you looking for? ")

worddict = words_count()

if search in worddict:
    print "Yep its in here!"
else:
    print "Nope, not in this document."
