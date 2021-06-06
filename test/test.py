import unittest
from calculator.calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_add(self):
        temp = Calculator()
        self.assertEqual(temp.add(2), 2)


    def test_subtract(self):
        temp = Calculator()
        self.assertEqual(temp.subtract(2), -2)


    def test_multiply(self):
        temp = Calculator()
        temp.value = 5
        self.assertEqual(temp.multiply(7), 35)


    def test_divide(self):
        temp = Calculator()
        temp.value = 5
        temp.multiply(7)
        self.assertEqual(temp.divide(7), 5)


    def test_root(self):
        temp = Calculator()
        temp.value = 9
        self.assertEqual(temp.root(2), 3)


    def test_reset(self):
        temp = Calculator()
        temp.value = 1
        self.assertFalse(temp.reset())

if __name__ == '__main__':
    unittest.main()


