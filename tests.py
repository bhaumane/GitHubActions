# Write a python program to perform unit testing on the sum_of_two_numbers function.
import unittest
from main import sum_of_two_numbers

class TestSumOfTwoNumbers(unittest.TestCase):
    def test_sum_of_two_numbers(self):
        self.assertEqual(sum_of_two_numbers(10, 20), 30)
        self.assertEqual(sum_of_two_numbers(-5, 5), 0)
        self.assertEqual(sum_of_two_numbers(0, 0), 0)
        self.assertEqual(sum_of_two_numbers(-10, -20), -30)

if __name__ == '__main__':
    unittest.main()

    