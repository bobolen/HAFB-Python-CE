"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count the number of words in document
Task 2: Count the number of times each word appears in the file
"""

from urllib.request import urlopen

#file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"


def word_count(url):
    """
    Retreives a file from http://icarus.cs.weber.edu/~hvalle/hafb/words.txt
    Prints the number of words in the file.
    Prints the number of times each word gets used in the file
    :param url: url to retrieve file from
    """

    file = url
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


def main():
    """
    Test function
    :return: nothing
    """
    word_count()


if __name__ == '__main__':
    main()
    exit()