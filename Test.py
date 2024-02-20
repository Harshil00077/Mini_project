#! /usr/bin/python3
import unittest
from calculator import addition, subtraction, multiplication, division, square_root, factorial, natural_logarithm, power

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        result = addition(10, 20)
        self.assertEqual(result, 30)
        
    def test_subtraction(self):
        result = subtraction(20, 10)
        self.assertEqual(result, 10)
        
    def test_multiplication(self):
        result = multiplication(5, 6)
        self.assertEqual(result, 30)
        
    def test_division(self):
        result = division(20, 5)
        self.assertEqual(result, 4)
        
        # Test division by zero
        result = division(20, 0)
        self.assertEqual(result, "Cannot divide by zero")
        
    def test_square_root(self):
        result = square_root(25)
        self.assertEqual(result, 5)
        
        # Test square root of negative number
        result = square_root(-25)
        self.assertEqual(result, "Can't take square root of negative number")
        
    def test_factorial(self):
        result = factorial(5)
        self.assertEqual(result, 120)
        
        # Test factorial of negative number
        result = factorial(-5)
        self.assertEqual(result, "Factorial of negative numbers is not defined.")
        
    def test_natural_logarithm(self):
        result = natural_logarithm(10)
        self.assertAlmostEqual(result, 2.302585092994046)
        
        # Test logarithm of negative number
        result = natural_logarithm(-10)
        self.assertEqual(result, "Cannot take log of negative or zero")
        
    def test_power(self):
        result = power(2, 3)
        self.assertEqual(result, 8)

        result = power(2,-1)
        self.assertEqual(result,0.5)

if __name__ == '__main__':
    unittest.main()
