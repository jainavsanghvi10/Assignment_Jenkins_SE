#!/usr/bin/python3
# Failing Test case for factorial

import unittest
from Palindrome import isPalindrome

class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(isPalindrome('Batman'), 1)

    def testCase2(self):
        self.assertEqual(isPalindrome('Science'), 1)


if __name__ == '__main__':
    unittest.main()
