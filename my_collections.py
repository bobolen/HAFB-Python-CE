"""
Learn about collections: Tuples, Strings, Range, List, Dictionaries, Sets
"""


def do_tuples():
    """
    Practice tuples
    :return: nothing
    """
    # Immutable sequence of arbitrary objects
    # Use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size", len(t))
    print("One member:", t[0])   # by index notation
    # To iterate over a tuple
    for item in t:
        print(item)

    # Single tuples must end with a comma
    t1 = (6,)
    print(t1, type(t1))
    # Another way to create tuples
    # Parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))
    # Tuple constructor: tuple()
    t_from_l = tuple([3, 77, 11])
    print(t_from_l, type(t_from_l))
    # Test for membership
    print(5 in (3, 6, 8, 5, 12))
    print(5 not in (3, 6, 8, 5, 12))


def min_max(items):
    """
    Return the minimum and maximum elements of a collection
    :param items: input collection
    :return: the minimum and maximum
    """
    return min(items), max(items)


def swap(n1, n2):
    """
    Swaps the contents of n1 and n2
    :param n1: input 1
    :param n2: input 2
    :return:
    """
    return n2, n1


def main():
    """
    Test function
    :return: 
    """
    do_tuples()
    # output = min_max([56, 76, 11, 12, 90])
    # print("min", output[0])
    # print("max", output[1])
    # # Tuple unpacking
    # lower, upper = min_max([56, 76, 11, 12, 90])
    # print("min", lower)
    # print("max", upper)
    # # Swap Values
    # a = "jelly"
    # b = "bean"
    # print(a, b)
    # # Call your function
    # a, b = swap(a, b)
    # print(a, b)


if __name__ == '__main__':
    main()
    exit(0)