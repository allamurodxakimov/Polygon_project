class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        return self.square_side>0 
    
    def area(self) -> float:
        """
        This method finds the area of the square.
        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        return self.square_side**2 if Square.is_valid(self)==True else False

    def perimeter(self) -> float:
        """
        This method finds the perimeter of the square.
        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        return self.square_side*4 if Square.is_valid(self)==True else False
kvadrat = Square(5.8)
print(kvadrat.is_valid())
print(kvadrat.area())
print(kvadrat.perimeter())
print(kvadrat.__class__)
print(dir(kvadrat.area()))
print(kvadrat.__format__)