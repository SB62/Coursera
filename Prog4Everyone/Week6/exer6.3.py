def count_string():
    word = raw_input("Please enter a word:")
    ltr = raw_input("Please enter a letter:")

    count = 0
    for letter in word:
        if letter == ltr:
            count = count + 1
    return count
count = count_string()
print count
