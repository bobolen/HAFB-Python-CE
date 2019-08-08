"""
A Flight Class.  Model for aircraft flights
"""


class Flight:
    """
    A flight with a particular passenger aircraft
    """
    def __init__(self, number):
        """
        Initializes Flight number
        :param number: flight number
        :raise: ValueError(For invalid format)
        """
        # implementataion delails begin with '_'
        # Validate flight number:
        # 6 chars loong: AADDD A->ALPHA, D->DIGIT
        if len(number) != 5:
            raise ValueError("Invalid flight number length {}".format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not number[2:3].isnumeric():
            raise ValueError("Invalid flight number {}".format(number))
        self._number = number

    def number(self):
        """
        Flight Number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        """
        Returns airline code
        :return: airline code
        """
        return self._number[:2]


class Aircraft:
    """

    """
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """
        Initializes Aircraft
        :param registration: registration number
        :param model: model number
        :param num_rows: number of rows in aircraft
        :param num_seats_per_row: number of seats per row
        """
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model


def main():
    """
    Test function
    :return: 
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)