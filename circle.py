from math import pi,fabs


class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        
        Args:
            No
        Returns:
            bool: True if the circle is valid, False otherwise
        """
        return self.radius>0 
    
    def diameter(self) -> float:
        '''
        This method finds the diameter of the circle.
        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        return self.radius *2 if Circle.is_valid(self) == True else False
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.
        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        return self.radius*2*pi if Circle.is_valid(self) == True else False 
    
    def area(self) -> float:
        '''
        This method finds the area of the circle.
        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        return self.radius*self.radius*pi if Circle.is_valid(self)==True else False
radius = Circle(4.5)
print(radius.is_valid())
print(radius.diameter())
print(radius.circumference())
print(radius.area())