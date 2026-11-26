#task 2 fractions

import math 

class Fraction:
    def __init__(self, numerator: int, denominator: int = 1) -> None:
        if not isinstance(numerator, int) or isinstance(numerator, bool):
            raise TypeError("numerator has to be an integer")
        if not isinstance(denominator, int) or isinstance(denominator, bool):
            raise TypeError("denominator has to be an integer")
        if denominator <= 0:
            raise ValueError("denominator must be positive / greater than 0")

        common = math.gcd(numerator, denominator)
        self._numerator = numerator = numerator // common 
        self._denominator = denominator // common
        
    @property
    def numerator(self) -> int: 
        return self._numerator 

    @property 
    def denominator(self) -> int:
        return self._denominator

    #string representation

    def __repr__(self) -> str:
        if self.denominator == 1:
            return f"Fraction({self.numerator})"
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self) -> str:
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    #arithmetic type conversion

    def __add__(self, other: "Fraction") -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented                                   
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented 
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented 
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("can't divide by a 0 fraction")
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        #alwasy keep this denmo,mnator positive if dividing nergative fraction, math rule blahblah
        if new_den < 0:
            new_num = -new_num
            new_den = -new_den
        return Fraction(new_num, new_den)

    def __neg__(self) -> "Fraction":
        return Fraction(-self.numerator, self.denominator)

    def __float__(self) -> float:
        return self.numerator / self.denominator    

    #the six rewuored comapøriposn ,method

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other: "Fraction") -> bool:
        if not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator * other.denominator >= other.numerator * self.denominator


  