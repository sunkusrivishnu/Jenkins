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
	'''result2 = factorial(data[1])
	result3 = factorial(data[2])
	result4 = factorial(data[3])
	result5 = factorial(data[4])
	result6 = factorial(data[5])'''
        self.assertEqual(result1, 1)
	'''self.assertEqual(result2, 1)
	self.assertEqual(result3, 2)
	self.assertEqual(result4, 6)
	self.assertEqual(result5, 24)
	self.assertEqual(result6, 120)'''
if __name__ == '__main__':
    unittest.main()
