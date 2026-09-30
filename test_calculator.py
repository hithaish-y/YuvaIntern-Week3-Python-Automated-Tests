import unittest
from calculator import add, subtract, multiply, divide, power, is_even


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_even_number(self):
        self.assertTrue(is_even(10))

    def test_odd_number(self):
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()