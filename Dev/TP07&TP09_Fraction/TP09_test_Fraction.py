import unittest
from TP07_Fraction import Fraction

class FactTestCase(unittest.TestCase) : 

    def test_init_fraction(self):
        test1 = Fraction(2,3)
        test2 = Fraction(8,13)
        test3 = Fraction(54,22)
        test4 = Fraction(186, 3823)
        self.assertEqual(test1, Fraction(2,3), 'Fraction init')
        self.assertEqual(test2, Fraction(8,13), 'Fraction init')
        self.assertEqual(test3, Fraction(54,22), 'Fraction init')
        self.assertEqual(test4, Fraction(186,3823), 'Fraction init')
        self.assertRaises(ValueError, Fraction, 2, 0)
        self.assertRaises(TypeError, Fraction, 2.0, 3)
        self.assertRaises(TypeError, Fraction, 2, 3.0)

    def test_str(self):
        test1 = Fraction(-2,3)
        test2 = Fraction(8,13)
        test3 = Fraction(54,22)
        test4 = Fraction(186, 3823)
        self.assertEqual(str(test1),'-2/3', 'Fraction str')
        self.assertEqual(str(test2),'8/13', 'Fraction str')
        self.assertEqual(str(test3),'27/11', 'Fraction str')
        self.assertEqual(str(test4),'186/3823', 'Fraction str')


    def test_as_mixed_number(self):
        test1 = Fraction(2,3)
        test2 = Fraction(-8,13)
        test3 = Fraction(54,22)
        test4 = Fraction(186, 3823)
        test5 = Fraction(901,2)
        self.assertEqual(str(test1.as_mixed_number()),'la fonction est propre et ne peux pas etre convertie en nombre mixte', 'Fraction mixed')
        self.assertEqual(str(test2.as_mixed_number()),'la fonction est propre et ne peux pas etre convertie en nombre mixte', 'Fraction mixed')
        self.assertEqual(str(test4.as_mixed_number()),'la fonction est propre et ne peux pas etre convertie en nombre mixte', 'Fraction mixed')
        self.assertEqual(str(test3.as_mixed_number()),'2*10/22', 'Fraction mixed')
        self.assertEqual(str(test5.as_mixed_number()),'450*1/2', 'Fraction mixed')

    def test_add(self):
        test1 = Fraction(-8,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        self.assertEqual((test1 + test2),Fraction(18,13), 'Fraction add')
        self.assertEqual((test2 + test3),Fraction(7832,3823), 'Fraction add')
        self.assertEqual((test1 + test3),Fraction(-28166,49699), 'Fraction add')
        self.assertEqual((test1 + 2),Fraction(18,13), 'Fraction add')
        self.assertEqual((test2 + 4),Fraction(6,1), 'Fraction add')
        self.assertEqual((test3 + 8),Fraction(30770,3823), 'Fraction add')
        self.assertEqual((test1 + 1592),Fraction(20688,13), 'Fraction add')

    def test_sub(self):
        test1 = Fraction(-8,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        self.assertEqual((test1 - test2),Fraction(-34,13), 'Fraction sub')
        self.assertEqual((test2 - test3),Fraction(7460,3823), 'Fraction sub')
        self.assertEqual((test1 - test3),Fraction(-33002,49699), 'Fraction sub')
        self.assertEqual((test1 - 2),Fraction(-34,13), 'Fraction sub')
        self.assertEqual((test2 - 4),Fraction(-2,1), 'Fraction sub')
        self.assertEqual((test3 - 8),Fraction(-30398,3823), 'Fraction sub')
        self.assertEqual((test1 - 1592),Fraction(-20704,13), 'Fraction sub')

    def test_mul(self):
        test1 = Fraction(-8,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        self.assertEqual((test1 * test2),Fraction(-16,13), 'Fraction mul')
        self.assertEqual((test2 * test3),Fraction(372,3823), 'Fraction mul')
        self.assertEqual((test1 * test3),Fraction(-1488,49699), 'Fraction mul')
        self.assertEqual((test1 * 2),Fraction(-16,13), 'Fraction mul')
        self.assertEqual((test2 * 4),Fraction(8,1), 'Fraction mul')
        self.assertEqual((test3 * 8),Fraction(1488,3823), 'Fraction mul')
        self.assertEqual((test1 * 1592),Fraction(-12736,13), 'Fraction mul')

    def test_truediv(self):
        test1 = Fraction(-8,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        self.assertEqual((test1 / test2),Fraction(-4,13), 'Fraction truediv')
        self.assertEqual((test2 / test3),Fraction(3823,93), 'Fraction truediv')
        self.assertEqual((test1 / test3),Fraction(-15292,1209), 'Fraction truediv')
        self.assertEqual((test1 / 2),Fraction(-4,13), 'Fraction truediv')
        self.assertEqual((test2 / 4),Fraction(1,2), 'Fraction truediv')
        self.assertEqual((test3 / 8),Fraction(93,15292), 'Fraction truediv')
        self.assertEqual((test1 / 1592),Fraction(-1,2587), 'Fraction truediv')
        with self.assertRaises(ValueError):
            Fraction(2,3) / Fraction(0,2)

    def test_pow(self):
        test1 = Fraction(-8,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        self.assertEqual((test1 ** test2),Fraction(64,169), 'Fraction power')
        self.assertEqual((test2 ** test3),Fraction(1,1), 'Fraction power')
        self.assertEqual((test1 ** 2),Fraction(64,169), 'Fraction power')
        self.assertEqual((test2 ** 4),Fraction(16,1), 'Fraction power')

    def test_eq(self):
        test1 = Fraction(2,3)
        test2 = Fraction(4,2)
        test3 = Fraction(4,6)
        self.assertEqual((test1 == test2),False, 'Fraction eq')
        self.assertEqual((test2 == test3),False, 'Fraction eq')
        self.assertEqual((test1 == test3),True, 'Fraction eq')
        self.assertEqual((test1 == test1),True, 'Fraction eq')
        self.assertEqual((test1 == 4),False, 'Fraction eq')
        self.assertEqual((test2 == 2),True, 'Fraction eq')
        self.assertEqual((test3 == 8),False, 'Fraction eq')

    def test_float(self):
        test1 = Fraction(-8,12)
        test2 = Fraction(4,2)
        test3 = Fraction(100, 1000)
        self.assertEqual(float(test1),-8/12, 'Fraction add')
        self.assertEqual(float(test2),4/2, 'Fraction add')
        self.assertEqual(float(test3),100/1000, 'Fraction add')

    def test_is_zero(self):
        test1 = Fraction(0,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        test4 = Fraction(0)
        self.assertEqual(test1.is_zero(),True, 'Fraction is_zero')
        self.assertEqual(test2.is_zero(),False, 'Fraction is_zero')
        self.assertEqual(test3.is_zero(),False, 'Fraction is_zero')
        self.assertEqual(test4.is_zero(),True, 'Fraction is_zero')

    def test_is_integer(self):
        test1 = Fraction(2,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        test4 = Fraction(55, 5)
        self.assertEqual(test1.is_integer(),False, 'Fraction is_integer')
        self.assertEqual(test2.is_integer(),True, 'Fraction is_integer')
        self.assertEqual(test3.is_integer(),False, 'Fraction is_integer')
        self.assertEqual(test4.is_integer(),True, 'Fraction is_integer')

    def test_is_proper(self):
        test1 = Fraction(2,13)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        test4 = Fraction(55, 5)
        self.assertEqual(test1.is_proper(),True, 'Fraction is_proper')
        self.assertEqual(test2.is_proper(),False, 'Fraction is_proper')
        self.assertEqual(test3.is_proper(),True, 'Fraction is_proper')
        self.assertEqual(test4.is_proper(),False, 'Fraction is_proper')

    def test_is_unit(self):
        test1 = Fraction(2,12)
        test2 = Fraction(4,2)
        test3 = Fraction(186, 3823)
        test4 = Fraction(55, 5)
        self.assertEqual(test1.is_unit(),True, 'Fraction is_unit')
        self.assertEqual(test2.is_unit(),False, 'Fraction is_unit')
        self.assertEqual(test3.is_unit(),False, 'Fraction is_unit')
        self.assertEqual(test4.is_unit(),False, 'Fraction is_unit')

    def test_is_adjacent_to(self):
        test1 = Fraction(2,12)
        test2 = Fraction(6,12)
        test3 = Fraction(186, 3823)
        test4 = Fraction(55, 5)
        self.assertEqual(test1.is_adjacent_to(test2),True, 'Fraction is_adjacent_to')
        self.assertEqual(test2.is_adjacent_to(test3),False, 'Fraction is_adjacent_to')
        self.assertEqual(test3.is_adjacent_to(test4),False, 'Fraction is_adjacent_to')
        self.assertEqual(test4.is_adjacent_to(test1),False, 'Fraction is_adjacent_to')
        self.assertEqual(test4.is_adjacent_to(12),True, 'Fraction is_adjacent_to')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
