#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from Prog1 import funct

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        
        result = funct(2,3)
        self.assertEqual(result, 7)
        
        result = funct(1,2)
        self.assertEqual(result, 4)
        
        result = funct(3,4)
        self.assertEqual(result, 10)
        
        result = funct(4,5)
        self.assertEqual(result, 13)
        
        result = funct(5,6)
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.main()
