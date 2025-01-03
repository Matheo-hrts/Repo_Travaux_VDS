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

        PRE : ?
        POST : ?
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

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : ?
        POST : ?
        """
        return f"{self.__num}/{self.__den}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : ?
        POST : ?
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

         PRE : ?
         POST : ?
         """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        new_num = self.__num * other.__den + other.__num * self.__den
        common_den = self.__den * other.__den

        return Fraction(new_num, common_den)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : ?
        POST : ?
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        new_num = self.__num * other.__den - other.__num * self.__den
        common_den = self.__den * other.__den
        return Fraction(new_num, common_den)


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : ?
        POST : ?
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        new_num = self.__num * other.__num
        new_den = self.__den * other.__den
        return Fraction(new_num, new_den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : ?
        POST : ?
        RAISES : ?
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        if(other.is_zero()) :
            raise ValueError('le denominateur ne peux être égale a 0')
        return self * Fraction(other.__den, other.__num)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : ?
        POST : ?
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        exp = other.__num / other.__den
        new_num = self.__num ** exp
        new_den = self.__den ** exp
        return Fraction(int(new_num), int(new_den))
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : ?
        POST : ?
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)
        
        return self.__num == other.__num and self.__den == other.__den

        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : ?
        POST : ?
        """
        return self.__num/self.__den
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : ?
        POST : ?
        """
        return self.__num == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : ?
        POST : ?
        """
        return (self.__num % self.__den) == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : ?
        POST : ?
        """
        return abs(self.__num) < abs(self.__den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : ?
        POST : ?
        """
        return self.__num == 1
        

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : ?
        POST : ?
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        num_diff = abs(self.__num * other.__den - self.__den * other.__num)
        den_diff = self.__den * other.__den
        gcd = math.gcd(num_diff, den_diff)
        reduced_num = num_diff // gcd
        reduced_den = den_diff // gcd
        return reduced_num == 1 and reduced_den > 0
