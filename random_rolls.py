"""
Simulate 6000 rolls of a die (1-6)
"""
import random
import statistics


def roll_die(num):
    """
    Random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 -> maps to 1
    Index 1 -> maps to 2
    etc
    """
    freq = [0] * 6    # empty list
    for roll in range(num):
        n = random.randint(1, 6)
        freq[n - 1] += 1
    return freq


def main():
    """
    Test function
    :return:
    """
    num = int(input("How many times do you want to roll the die?"))
    result = roll_die(num)
    for roll, total in enumerate(result):
        print("Total rolls of {} = {}".format(roll, total))

    print("Average = {}".format(sum(result)/len(result)))
    print("Mean = {}".format(statistics.mean(result)))
    print("Median = {}".format(statistics.median(result)))


if __name__ == '__main__':
    main()
    exit(0)