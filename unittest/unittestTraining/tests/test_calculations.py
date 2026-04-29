import unittest

from src.calculations import add , sub , mul

class TestCalculation(unittest.TestCase):
    def test_add(self):
        res = add(10 ,5)
        self.assertEqual(res, 15, msg='Addition Error')

    def test_sub(self):
        res = add(10, 5)
        self.assertEqual(res, 5, msg='Substraction Error')

    def test_mul(self):
        res = add(10, 5)
        self.assertEqual(res, 50, msg='Multiplication Error')

