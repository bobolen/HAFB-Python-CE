"""
Use flight class
"""
from airtravel import Flight, Aircraft


def main():
    """
    Test function
    :return: 
    """
    f = Flight("SN066")
    print(f.number(), f.airline())
    # f2 = flight("ab345")
    f2 = Flight("SN345")
    print(f2.number(), f2.airline())
    # Could use: Flight.number(f)
    a1 = Aircraft("G-EUP", "Airbus A319", num_rows=22, num_seats_per_row=6)
    print(a1.registration(), a1.model())



if __name__ == '__main__':
    main()
    exit(0)