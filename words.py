"""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task 1: Count the number of words in document
Task 2: Count the number of times each word appears in the file
"""
from urllib.request import urlopen


def word_count(url):
    """
    Retreives a file from http://icarus.cs.weber.edu/~hvalle/hafb/words.txt
    Prints the number of words in the file.
    Prints the number of times each word gets used in the file
    :param url: url to retrieve file from
    """


    count = 0
    data = []
    with urlopen(url) as story:
        for line in story:
            words = line.decode('utf-8').split()    # split with space as separator
            # print(words)
            for word in words:
                data.append(word)
    return data


def print_items(items):
    """
    print elements of the collection
    :param story_words: A collection of objects
    :return: nothing
    """
    for item in items:
        print(item)

def main():
    """
    Test function
    :return: nothing
    """
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = word_count(file)
    print_items(words)


if __name__ == '__main__':
    main()
    exit()