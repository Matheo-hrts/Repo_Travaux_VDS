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
        POST : 'self.numerator' and 'self.denominator'
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
        if(type(new_num) != int) :
            raise TypeError('The numerator need to be an integer')
        self.__num = new_num

    @denominator.setter
    def denominator(self, new_den : int) :
        if(type(new_den) != int) :
            raise ValueError('The denominator need to be an integer')
        elif(new_den == 0) :
            raise ValueError('The denominator cannot be 0')
        else :
            self.__den = new_den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : '__num' and '__den'
        POST : a string that represent the reduced form of the fraction
        """
        gcd = math.gcd(self.__num, self.__den)
        reduced_num = self.__num // gcd
        reduced_den = self.__den // gcd
        return f"{reduced_num}/{reduced_den}"

    def as_mixed__number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : '__num' and '__den'
        POST : a mixed number
        """
        if(self.__num < self.__den):
            return 'la fonction est propre et ne peux pas etre convertie en nombre mixte'
        else :
            quotient = self.__num // self.__den
            remainder = self.__num - self.__den * quotient
            return f'le nombre mixte de cette fraction est {quotient}*{remainder}/{self.__den}.'

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : '__num' and '__den', 'other.__num' and 'other.__den'
         POST : return a fraction class with the new_num an common_den after adding  one to another
         """
        new_num = self.__num * other.__den + other.__num * self.__den
        common_den = self.__den * other.__den

        return Fraction(new_num, common_den)


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : '__num' and '__den', 'other.__num' and 'other.__den'
        POST : return a fraction class with the new_num an common_den after substracting one to another
        """
        new_num = self.__num * other.__den - other.__num * self.__den
        common_den = self.__den * other.__den
        return Fraction(new_num, common_den)


    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : '__num' and '__den', 'other.__num' and 'other.__den'
        POST : return a fraction class with the new_num an new_den after multiplying them
        """
        new_num = self.__num * other.__num
        new_den = self.__den * other.__den
        return Fraction(new_num, new_den)


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : '__num' and '__den', 'other.__num' and 'other.__den'
        POST : return the multiply of the first by the invert second fraction
        """
        if(other.is_zero()) :
            raise ValueError('le __denominateur ne peux être égale a 0')
        return self * Fraction(other.__den, other.__num)


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : '__num' and '__den', 'other.__num' and 'other.__den'
        POST : return a fraction class with new_num and new_den after applying the power
        """
        exp = int(other.__num / other.__den)
        new_num = self.__num ** exp
        new_den = self.__den ** exp
        return Fraction(new_num, new_den)
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : '__num' and '__den', 'other.__num' and 'other.__den'
        POST : return a boolean that say if the two fraction are equivalent when they are redueced
        
        """
        gcd_self = math.gcd(self.__num, self.__den)
        gcd_other = math.gcd(other.__num, other.__den)
        reduced_self__num = self.__num // gcd_self
        reduced_self___den = self.__den // gcd_self
        reduced_other__num = other.__num // gcd_other
        reduced_other___den = other.__den // gcd_other
        return reduced_self__num == reduced_other__num and reduced_self___den == reduced_other___den

        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : '__num' and '__den'
        POST : return the float version of the fraction
        """
        return self.__num/self.__den
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : '__num'
        POST : return a bolean to know if the fraction value is zero
        """
        return self.__num == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : '__num' and '__den'
        POST : a boolean to know if the fraction is an integer
        """
        return (self.__num % self.__den) == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : '__num' and '__den'
        POST : a boolean to know if the obsolute fraction of the fraction is < than 1
        """
        return abs(self.__num) < abs(self.__den)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : '__num' and '__den'
        POST : a boolean to know if the numerator is one in its reduced form
        """
        gcd = math.gcd(self.__num, self.__den)
        return (self.__num // gcd) == 1
        

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : '__num' and '__den', 'other.__num' and 'other.__den'
        POST : a boolean to know if the absolute value of the difference between self and other is a unit fraction
        """
        num_diff = abs(self.__num * other.__den - self.__den * other.__num)
        __den_diff = self.__den * other.__den
        gcd = math.gcd(num_diff, __den_diff)
        reduced__num = num_diff // gcd
        reduced___den = __den_diff // gcd
        return reduced__num == 1 and reduced___den > 0
