#!/usr/bin/python3
# Passing Test case for checking factorial of numbers

import unittest
from Palindrome import isPalindrome


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(isPalindrome('radar'), 1)

    def testCase2(self):
        self.assertEqual(isPalindrome('malayalam'), 1)

    def testCase3(self):
        self.assertEqual(isPalindrome('aaabccbaaa'), 1)


if __name__ == '__main__':
    unittest.main()
