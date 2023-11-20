class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def is_valid(self) -> bool:
        """
        This method checks if the rectangle is valid
        
        Args:
            No
        Returns: 
            bool: True if the rectangle is valid, False otherwise
        """ 
        return True if self.a>0 and self.b>0 else False
    def perimeter(self) -> float:
        """
        This method finds the perimeter of the rectangle.
        Args:
            No
        Returns:
            float or int: return perimeter of the rectangle if the rectangle is valid, 0 otherwise
        """
        return 2*(self.a + self.b) if Rectangle.is_valid(self)==True else False

    def area(self) -> float:
        """
        This method finds the area of the rectangle.
        Args:
            No
        Returns:
            float or int:  return area of the rectangle if the rectangle is valid, 0 otherwise 
        """
        return self.a * self.b if Rectangle.is_valid(self) else False
rectang = Rectangle(2.5 , 2)
print(rectang.is_valid())
print(rectang.perimeter())
print(rectang.area())
