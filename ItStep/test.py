import unittest
from main import celsius_to_fahrenheit
from main import fahrenheit_to_celsius
from main import is_palindrome
from main import reverse_string


class TestCelsius(unittest.TestCase):
    def test_celsius(self):
        x = celsius_to_fahrenheit
        self.assertEqual(x(0), 32)

    def test_calsius_not_equal(self):
        x = celsius_to_fahrenheit
        self.assertNotEqual(x(0), 31)


class TestFahrenheit(unittest.TestCase):
    def test_fahrenheit(self):
        y = fahrenheit_to_celsius
        self.assertEqual(y(0), -17.77777777777778)

    def test_fahrenheit_not_equal(self):
        y = fahrenheit_to_celsius
        self.assertNotEqual(y(0), 18)


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        z = is_palindrome('')
        self.assertTrue(z, 'level')


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        e = reverse_string('hi')
        self.assertEqual(e, 'ih')


