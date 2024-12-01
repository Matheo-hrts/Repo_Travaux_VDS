import unittest
from TP07_Fraction import Fraction

class FactTestCase(unittest.TestCase) : 

    def test_init_fraction(self):
        test1 = Fraction(2,3)
        self.assertEqual(test1, Fraction(2,3), 'Fraction init')

    def test_strings(self):
        test1 = Fraction(2,3)
        test2 = Fraction(7,3)
        self.assertEqual(str(test1),'2/3', 'Fraction str')
        self.assertEqual(str(test1.as_mixed_number()),'la fonction est propre et ne peux pas etre convertie en nombre mixte', 'Fraction mixed')
        self.assertEqual(str(test2.as_mixed_number()),'2*1/3', 'Fraction mixed')

    def test_fraction_oparators_with_two_fractions(self):
        test1 = Fraction(2,3)
        test2 = Fraction(3,2)
        test3 = Fraction(4,6)
        self.assertEqual((test1 + test2),Fraction(13,6), 'Fraction add')
        self.assertEqual((test1 - test2),Fraction(-5,6), 'Fraction sub')
        self.assertEqual((test1 * test2),Fraction(1,1), 'Fraction mul')
        self.assertEqual((test1 / test2),Fraction(4,9), 'Fraction truediv')
        self.assertEqual((test1 ** test2),Fraction(2,5), 'Fraction power')
        self.assertEqual((test1 == test2),False, 'Fraction eq False')
        self.assertEqual((test1 == test3),True, 'Fraction eq True')
        self.assertEqual((float(test1)),2/3, 'Fraction float')

    def test_fraction_operators_with_other_as_int(self):
        test1 = Fraction(2, 3)
        test2 = Fraction(2, 1)
        self.assertEqual((test1 + 2),Fraction(8,3), 'Fraction add')
        self.assertEqual((test1 - 2),Fraction(-4,3), 'Fraction sub')
        self.assertEqual((test1 * 2),Fraction(4,3), 'Fraction mul')
        self.assertEqual((test1 / 2),Fraction(1,3), 'Fraction div')
        self.assertEqual((test1 ** 2),Fraction(4,9), 'Fraction power')
        self.assertEqual((test1 == 2),False, 'Fraction eq False')
        self.assertEqual((test2 == 2),True, 'Fraction eq True')
        self.assertEqual((test1.is_adjacent_to(2)),False, 'Fraction is_adjacent_to False')
        self.assertEqual((test2.is_adjacent_to(1)),True, 'Fraction is_adjacent_to True')

    
    def test_fraction_properties(self):
        test1 = Fraction(2,3)
        test2 = Fraction(3,2)
        test3 = Fraction(0,5)
        test4 = Fraction(8,4)
        test5 = Fraction(2,4)
        test6 = Fraction(3,4)
        test7 = Fraction(5,4)
        self.assertEqual((test1.is_zero()),False, 'Fraction is_zero False')
        self.assertEqual((test3.is_zero()),True, 'Fraction is_zero True')
        self.assertEqual((test1.is_integer()),False, 'Fraction is_integer False')
        self.assertEqual((test4.is_integer()),True, 'Fraction is_integer True')
        self.assertEqual((test2.is_proper()),False, 'Fraction is_proper False')
        self.assertEqual((test1.is_proper()),True, 'Fraction is_proper True')
        self.assertEqual((test1.is_unit()),False, 'Fraction is_unit False')
        self.assertEqual((test5.is_unit()),True, 'Fraction is_unit True')
        self.assertEqual((test1.is_adjacent_to(test7)),False, 'Fraction is_adjacent_to False')
        self.assertEqual((test6.is_adjacent_to(test7)),True, 'Fraction is_adjacent_to True')

    def test_fraction_div_0(self):
        self.assertRaises(ValueError, Fraction, 2, 0)
        self.assertRaises(TypeError, Fraction, 2.0, 3)
        self.assertRaises(TypeError, Fraction, 2, 3.0)
        with self.assertRaises(ValueError):
            Fraction(2,3) / Fraction(0,2)
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
