import unittest
from unittesting.func import calc

class TestCalc(unittest.TestCase):
    
    def test_add_valid(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_sub_valid(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)

    def test_multiply_valid(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)

    def test_divide_valid(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)
        self.assertEqual(calc.divide(5,2),2.5)

    def test_divide_exception(self):
        self.assertRaises(ValueError,calc.divide,10,0)
        with self.assertRaises(ValueError):
            calc.divide(10,0)