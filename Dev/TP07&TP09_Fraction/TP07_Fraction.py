import math

"""Ce code a été réalisé avec l'aide de chatGPT"""

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van __den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : '__num' and '__den' are integers
        POST : 'self.numerator' and 'self.denominator' force the use of the setters to run verification on type
        """
        self.__num = None
        self.__den = None
        self.numerator = num
        self.denominator = den

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den
    
    @numerator.setter
    def numerator(self, new_num : int) :
        """This set the numerator to a value.

        PRE : 'new_num' is an integers.
        POST : '__num' is set.
        RAISES : TypeError is 'new_num' is not an integer.
        """
        if(type(new_num) != int) :
            raise TypeError('The numerator need to be an integer')
        self.__num = new_num

    @denominator.setter
    def denominator(self, new_den : int) :
        """This set the denominator to a value.

        PRE : 'new_den' is an integers.
        POST : '__den' is set.
        RAISES : TypeError if 'new_den' is not an integer. 
                 ValueError if 'new_den' is equal to 0.
        """
        if(type(new_den) != int) :
            raise TypeError('The denominator need to be an integer')
        elif(new_den == 0) :
            raise ValueError('The denominator cannot be 0')
        else :
            self.__den = new_den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : None.
        POST : Return a string that represent the reduced form of the fraction.
        """
        gcd = math.gcd(self.__num, self.__den)
        reduced_num = self.__num // gcd
        reduced_den = self.__den // gcd
        return f"{reduced_num}/{reduced_den}"

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : None.
        POST : A string that represent the fraction as a mixed number.
        """
        if(self.__num < self.__den):
            return 'la fonction est propre et ne peux pas etre convertie en nombre mixte'
        else :
            quotient = self.__num // self.__den
            remainder = self.__num - self.__den * quotient
            return f'{quotient}*{remainder}/{self.__den}'

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : 'other' is an integer or an instance of Fraction.
         POST : Return an instance of a fraction that is the addition of self and other.
         """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        new_num = self.__num * other.__den + other.__num * self.__den
        common_den = self.__den * other.__den

        return Fraction(new_num, common_den)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : 'other' is an integer or an instance of Fraction.
        POST : Return an instance of a fraction that is the difference of self and other.
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        new_num = self.__num * other.__den - other.__num * self.__den
        common_den = self.__den * other.__den
        return Fraction(new_num, common_den)


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : 'other' is an integer or an instance of Fraction.
        POST : Return an instance of a fraction that is the product of self and other.
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        new_num = self.__num * other.__num
        new_den = self.__den * other.__den
        return Fraction(new_num, new_den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : 'other' is an integer or an instance of Fraction.
        POST : Return an instance of a fraction that is the quotient of self and other.
        RAISES : ValueError if other is 0.
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        if(other.is_zero()) :
            raise ValueError('le __denominateur ne peux être égale a 0')
        return self * Fraction(other.__den, other.__num)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : 'other' is an integer or an instance of Fraction.
        POST : Return an instance of a fraction that is self to the power of other.
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        exp = other.__num / other.__den
        new_num = self.__num ** exp
        new_den = self.__den ** exp
        return Fraction(int(new_num), int(new_den))
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : 'other' is an integer or an instance of Fraction.
        POST : Return True if the reduced form of self and other are the same, False if not.
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)
        
        gcd_self = math.gcd(self.__num, self.__den)
        gcd_other = math.gcd(other.__num, other.__den)
        reduced_self_num = self.__num // gcd_self
        reduced_self_den = self.__den // gcd_self
        reduced_other_num = other.__num // gcd_other
        reduced_other_den = other.__den // gcd_other
        return reduced_self_num == reduced_other_num and reduced_self_den == reduced_other_den

        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : None.
        POST : Return the decimal value of the fraction.
        """
        return self.__num/self.__den
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : None.
        POST : Return True if the fraction value is zero, False if not.
        """
        return self.__num == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : None.
        POST : Return True if the fraction is an integer, False if not.
        """
        return (self.__num % self.__den) == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : None.
        POST : Return True if the absolute value of the fraction is lower than 1, False if not.
        """
        return abs(self.__num) < abs(self.__den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : None.
        POST : Return True if the fraction's numerator is 1 in its reduced form, False if not.
        """
        gcd = math.gcd(self.__num, self.__den)
        return (self.__num // gcd) == 1
        

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : 'other' is an integer or an instance of Fraction.
        POST : Return True if the difference between the absolute of self and other is a unit fraction, False if not.
        """
        if not isinstance(other, Fraction) :
            other = Fraction(other)

        num_diff = abs(self.__num * other.__den - self.__den * other.__num)
        den_diff = self.__den * other.__den
        gcd = math.gcd(num_diff, den_diff)
        reduced_num = num_diff // gcd
        reduced_den = den_diff // gcd
        return reduced_num == 1 and reduced_den > 0
