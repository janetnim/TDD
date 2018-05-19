def add(x, y):
    return x + y


def area(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    return x/y

import unittest


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
