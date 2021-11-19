#!/usr/bin/python3
# Test case for finding factorial of a number
import unittest

from Prog1 import factorial

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to find factorial of given numbers
        """
        data = [0, 1, 2, 3, 4, 5]
        result1 = factorial(data[0])
        self.assertEqual(result1, 1)
if __name__ == '__main__':
    unittest.main()
