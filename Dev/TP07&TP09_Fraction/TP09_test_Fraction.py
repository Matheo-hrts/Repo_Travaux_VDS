import unittest
import math
from TP07_Fraction import Fraction

class FactTestCase(unittest.TestCase) : 
    def test_fraction_oparators(self):
        test1 = Fraction(2,3)
        test2 = Fraction(3,2)
        test3 = Fraction(4,6)
        self.assertEqual(str(test1),'2/3', 'Fraction str')
        self.assertEqual(str(test1 + test2),'13/6', 'Fraction add')
        self.assertEqual(str(test1 - test2),'-5/6', 'Fraction sub')
        self.assertEqual(str(test1 * test2),'1/1', 'Fraction mul')
        self.assertEqual(str(test1 / test2),'4/9', 'Fraction truediv')
        self.assertEqual(str(test1 ** test2),'2/5', 'Fraction power')
        self.assertEqual(str(test1 == test2),'False', 'Fraction eq False')
        self.assertEqual(str(test1 == test3),'True', 'Fraction eq True')
        self.assertEqual(str(float(test1)),str(2/3), 'Fraction float')
    
    def test_fraction_properties(self):
        test1 = Fraction(2,3)
        test2 = Fraction(3,2)
        test3 = Fraction(0,5)
        test4 = Fraction(8,4)
        test5 = Fraction(2,4)
        test6 = Fraction(3,4)
        test7 = Fraction(5,4)
        self.assertEqual(str(test1.is_zero()),'False', 'Fraction is_zero False')
        self.assertEqual(str(test3.is_zero()),'True', 'Fraction is_zero True')
        self.assertEqual(str(test1.is_integer()),'False', 'Fraction is_integer False')
        self.assertEqual(str(test4.is_integer()),'True', 'Fraction is_integer True')
        self.assertEqual(str(test2.is_proper()),'False', 'Fraction is_proper False')
        self.assertEqual(str(test1.is_proper()),'True', 'Fraction is_proper True')
        self.assertEqual(str(test1.is_unit()),'False', 'Fraction is_unit False')
        self.assertEqual(str(test5.is_unit()),'True', 'Fraction is_unit True')
        self.assertEqual(str(test1.is_adjacent_to(test7)),'False', 'Fraction is_adjacent_to False')
        self.assertEqual(str(test6.is_adjacent_to(test7)),'True', 'Fraction is_adjacent_to True')

    def test_fraction_div_0(self):
        self.assertRaises(ValueError, Fraction, (2,0))
        

if __name__ == '__main__':
    # ATTENTION : Pour exécuter ce test dans un notebook, il faut utiliser un appel à unittest.main() modifié. 
    # Dans PyCharm, vous pouvez utiliser la version normale sans paramètre, cfr ci-dessous.  
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
