from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        return self.a + self.b > self.c and self.c + self.b > self.a and  self.a + self.c > self.b and self.a > 0 and self.b > 0 and self.c > 0 
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        return False if Triangle.is_valid(self)==False else "Teng yonli" if (self.a == self.b and self.a != self.c ) or (self.c == self.b and self.a != self.c ) or (self.a == self.c and self.b != self.c ) else "Teng tomonli ):" if self.a == self.b and self.b == self.c else "Turli tomonli ):"
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a + self.b + self.c if Triangle.is_valid(self)==True else False

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a * self.b * self.c if Triangle.is_valid(self) == True else False
uchburchak = Triangle(3,4,5)
print(uchburchak.is_valid())
print(uchburchak.get_type())
print(uchburchak.perimeter())
print(uchburchak.area())