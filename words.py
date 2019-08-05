"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count the number of words in document
Task 2: Count the number of times each word appears in the file
"""
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
from functions import even_or_odd

count = 0
dictionary = {}
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()    # split with space as separator
        # print(words)
        for word in words:
            count += 1
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
print("Total number of words is", count)
# Sort by key values
for key in sorted(dictionary.keys()):
    print(key, dictionary[key])
# print(dictionary)

even_or_odd(count)