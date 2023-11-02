def sum_even(numbers):
    return sum(n for n in numbers if n % 2 == 0)

def factorial_simple(n):
    if n == 0:
        return 1
    return n * factorial_simple(n - 1)

def is_palindrome_simple(s):
    return s == s[::-1]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max(numbers):
    return max(numbers)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_char(s, char):
    return s.count(char)

def first_non_repeated(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

import unittest

class TestFunctions(unittest.TestCase):

    def test_sum_even(self):
        self.assertEqual(sum_even([1, 2, 3, 4]), 6)
        self.assertEqual(sum_even([-2, -4, 5]), -6)
        self.assertEqual(sum_even([]), 0)

    def test_factorial_simple(self):
        self.assertEqual(factorial_simple(5), 120)
        self.assertEqual(factorial_simple(0), 1)
        self.assertEqual(factorial_simple(7), 5040)

    def test_is_palindrome_simple(self):
        self.assertTrue(is_palindrome_simple("radar"))
        self.assertFalse(is_palindrome_simple("hello"))
        self.assertTrue(is_palindrome_simple("a"))

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 3]), 5)
        self.assertEqual(find_max([-1, -5, -3]), -1)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(7), 5040)

    def test_count_char(self):
        self.assertEqual(count_char("hello", "l"), 2)
        self.assertEqual(count_char("hello", "z"), 0)

    def test_first_non_repeated(self):
        self.assertEqual(first_non_repeated("swiss"), "w")
        self.assertEqual(first_non_repeated("repeated"), "a")
        self.assertIsNone(first_non_repeated("aabbcc"))

    def test_are_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertFalse(are_anagrams("hello", "world"))

if __name__ == "__main__":
    unittest.main()
