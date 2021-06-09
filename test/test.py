import unittest
from calculator.calculator import Calculator


class MyTestCase(unittest.TestCase):
    def test_add(self) -> None:
        temp = Calculator()
        self.assertEqual(temp.add(2), 2)

    def test_subtract(self) -> None:
        temp = Calculator()
        self.assertEqual(temp.subtract(2), -2)

    def test_multiply(self) -> None:
        temp = Calculator()
        temp.value = 5
        self.assertEqual(temp.multiply(7), 35)

    def test_divide(self) -> None:
        temp = Calculator()
        temp.value = 35
        self.assertEqual(temp.divide(7), 5)

    def test_root(self) -> None:
        temp = Calculator()
        temp.value = 9
        self.assertEqual(temp.root(2), 3)

    def test_root_zero(self) -> None:
        temp = Calculator()
        self.assertEqual(temp.root(0),1)

    def test_reset(self) -> None:
        temp = Calculator()
        temp.value = 86
        self.assertFalse(temp.reset())


if __name__ == "__main__":
    unittest.main()
