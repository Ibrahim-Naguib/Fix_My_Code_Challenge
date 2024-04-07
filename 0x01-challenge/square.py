#!/usr/bin/python3
# Square class module


class Square():
    """
    A class representing a square shape.

    Attributes:
    - width: The width of the square.
    - height: The height of the square.
    """
    def __init__(self, side_length):
        """
        Initializes a square with the given side length.

        Args:
        - side_length (int): The length of a side of the square.
        """
        self.side_length = side_length

    def area_of_my_square(self):
        """ Area of the square """
        return self.side_length * self.side_length

    def PermiterOfMySquare(self):
        """Calculates the perimeter of the square."""
        return 4 * self.side_length

    def __str__(self):
        """Returns a string representation of the square"""
        return "{}/{}".format(self.side_length, self.side_length)


if __name__ == "__main__":

    s = Square(side_length=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
