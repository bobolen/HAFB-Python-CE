"""
Learn about scoping in Python
"""
count = 0   # global object


def set_count(n):
    """
    Set global counter to n
    :param n: set count to n
    :return: nothing
    """
    global count
    count = n


def show_count():
    """
    Display the current count
    :return: nothing
    """
    print(count)


def main():
    """
    Test function
    :return: 
    """
    show_count()
    set_count(3)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)