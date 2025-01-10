import math

"""Ce code a été réalisé avec l'aide de chatGPT"""

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num and den are integers.
        POST : The fraction is initialized in its reduced form.
        RAISE : TypeError if num or den are not integers.
                ValueError if den is 0.
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Numerator and denominator must be integers.")
        if den == 0:
            raise ValueError("Denominator cannot be 0.")
        
        if den < 0:
            num, den = -num, -den
        
        gcd = math.gcd(num, den)
        self.__num = num // gcd
        self.__den = den // gcd

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

# ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : None.
        POST : Returns a string representation in the form "num/den".
        """
        return f"{self.__num}/{self.__den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction.

        PRE : None.
        POST : Returns a string representation as a mixed number or fraction.
        """
        if abs(self.__num) < self.__den:
            return str(self)
        
        whole = self.__num // self.__den
        remainder = abs(self.__num) % self.__den
        if remainder == 0:
            return str(whole)
        return f"{whole}*{remainder}/{self.__den}"

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : None.
        POST : Returns a new Fraction representing the sum.
        RAISE : ValueError if other is not an int or a fraction or convertible to an int.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)

        new_num = self.__num * other.__den + other.__num * self.__den
        common_den = self.__den * other.__den

        return Fraction(new_num, common_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : None.
        POST : Returns a new Fraction representing the difference.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)

        new_num = self.__num * other.__den - other.__num * self.__den
        common_den = self.__den * other.__den
        return Fraction(new_num, common_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : None.
        POST : Returns a new Fraction representing the product.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)

        new_num = self.__num * other.__num
        new_den = self.__den * other.__den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : None.
        POST : Returns a new Fraction representing the quotient.
        RAISE : ValueError if other is zero.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)

        if other.is_zero():
            raise ValueError("Denominator cannot be zero.")
        return self * Fraction(other.__den, other.__num)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : None.
        POST : Returns a new Fraction representing the power.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)

        exp = other.__num / other.__den
        new_num = self.__num ** exp
        new_den = self.__den ** exp
        return Fraction(int(new_num), int(new_den))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : None.
        POST : Returns True if the fractions are equal, False otherwise.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        return self.__num == other.__num and self.__den == other.__den

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : None.
        POST : Returns the decimal representation of the fraction.
        """
        return self.__num / self.__den

# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None.
        POST : Returns True if the fraction is 0, False otherwise.
        """
        return self.__num == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None.
        POST : Returns True if the fraction is an integer, False otherwise.
        """
        return (self.__num % self.__den) == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None.
        POST : Returns True if the fraction is proper, False otherwise.
        """
        return abs(self.__num) < abs(self.__den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None.
        POST : Returns True if the numerator is 1, False otherwise.
        """
        return self.__num == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : None.
        POST : Returns True if the fractions are adjacent, False otherwise.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)

        num_diff = abs(self.__num * other.__den - self.__den * other.__num)
        den_diff = self.__den * other.__den
        gcd = math.gcd(num_diff, den_diff)
        reduced_num = num_diff // gcd
        reduced_den = den_diff // gcd
        return reduced_num == 1 and reduced_den > 0
