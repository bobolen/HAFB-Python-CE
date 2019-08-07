"""
List Comprehensions
Readable, expressive, and effective
"""
from math import factorial, sqrt
from pprint import pprint as pp


def is_prime(n):
    """
    Figures out if a number is prime or not
    :param n: input number
    :return: True if prime
            False if not prime
    """
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False

    return True


def main():
    """
    Test function
    :return:
    """
    words = "Today I am very happy to learn about list comprehensions".split()
    print(words)
    data = []   # empty list
    for word in words:
        # Some analysis ...
        data.append(word)
    # "Filter" data
    print(data)

    # Task: find the length of the first 20
    # Factorial numbers
    info = []
    for x in range(200):
        # print(factorial(x))
        info.append(len(str(factorial(x))))
    # Print info
    pp(info)
    # Use a list comprehension: [ ]
    info2 = [len(str(factorial(x))) for x in range(200)]
    pp(info2)

    # Set comprehensions: { }
    info3 = {len(str(factorial(x))) for x in range(200)}
    pp(info3)

    # Dictionary Comprehensions:
    nba_teams = {'jazz':'SLC', 'warriors':'OAKLAND', 'lakers':'LA', 'clippers':'LA'}
    pp(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # Filter predicates
    primes = [x for x in range(1000001) if is_prime(x)]
    print(len(primes), primes)


if __name__ == '__main__':
    main()
    exit(0)