from decimal import Decimal
import math
class Square:
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError('Side length must be greater than 0.')
        self._side = side

    @property
    def side(self) -> float:
        return self._side

    @property
    def perimeter(self) -> float:
        return 4 * self._side

    @property
    def area(self) -> float:
        return self._side ** 2

    @property
    def diagonal(self) -> float:
        return math.sqrt(2 * self._side ** 2)

    def __repr__(self):
        return (f'Square({self.side})')

    def __str__(self):
        return f'Side={self.side},Perimeter={self.perimeter},Area={self.area},Diagonal={self.diagonal}'


square = Square(5)
print(square)

