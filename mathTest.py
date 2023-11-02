def generate_primes(N):
    primes = []
    for num in range(2, N):
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
    return primes

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)


def fibonacci(N):
    if N <= 1:
        return [0, 1][:N]
    sequence = [0, 1]
    while len(sequence) < N:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def matrix_multiplication(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions don't match for multiplication")
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

import mathTest

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return ()
    elif delta == 0:
        return (-b / (2*a),)
    else:
        return ((-b + math.sqrt(delta)) / (2*a), (-b - math.sqrt(delta)) / (2*a))

def collatz(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3*n + 1
        sequence.append(n)
    return sequence

import random

def approximate_pi(samples):
    inside_circle = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
    return 4 * inside_circle / samples

def totient(n):
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result

def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] |= dp[i - num]
    return dp[target]
import unittest

class TestMathFunctions(unittest.TestCase):

    # Tests for generate_primes
    def test_generate_primes(self):
        self.assertEqual(generate_primes(10), [2, 3, 5, 7])
        self.assertEqual(generate_primes(2), [])
        self.assertEqual(generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

    # Tests for gcd
    def test_gcd(self):
        self.assertEqual(gcd(14, 28), 14)
        self.assertEqual(gcd(18, 24), 6)
        self.assertEqual(gcd(5, 7), 1)

    # Tests for factorial
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(7), 5040)

    # Tests for fibonacci
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])

    # Tests for matrix_multiplication
    def test_matrix_multiplication(self):
        self.assertEqual(matrix_multiplication([[1,2],[3,4]], [[2,0],[1,3]]), [[4,6],[10,12]])
        with self.assertRaises(ValueError):
            matrix_multiplication([[1,2,3],[4,5,6]], [[1,2],[3,4]])

    # Tests for solve_quadratic
    def test_solve_quadratic(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (2.0, 1.0))
        self.assertEqual(solve_quadratic(1, 0, -1), (1.0, -1.0))
        self.assertEqual(solve_quadratic(1, 0, 1), ())

    # Tests for collatz
    def test_collatz(self):
        self.assertEqual(collatz(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])

    # Tests for approximate_pi
    # Note: It's a probabilistic method, so results can vary. Just ensure it's close to Pi.
    def test_approximate_pi(self):
        self.assertAlmostEqual(approximate_pi(100000), 3.14, 2)

    # Tests for totient
    def test_totient(self):
        self.assertEqual(totient(9), 6)
        self.assertEqual(totient(10), 4)

    # Tests for can_partition
    def test_can_partition(self):
        self.assertTrue(can_partition([1, 5, 11, 5]))
        self.assertFalse(can_partition([1, 2, 3, 5]))

if __name__ == "__main__":
    unittest.main()

