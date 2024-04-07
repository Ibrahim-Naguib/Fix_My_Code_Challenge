#!/usr/bin/python3
# Square class module


class Square():
    """
    A class representing a square.

    Attributes:
    width (int): The width of the square.
    height (int): The height of the square.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the Square object.

        Args:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of the square.

        Returns:
        int: The perimeter of the square.
        """
        return self.width * 4

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
        str: A string representing the square's dimensions.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
