import unittest
from palindrome import palindrome
class TestPalindrome(unittest.TestCase):
    def testPalindromeUno(self):
        result = palindrome('nequen')
        self.assertEqual(result, True)     
class TestPalindrome(unittest.TestCase):
    def testPalindromeDos(self):
        result = palindrome('Di clases al Cid')
        self.assertEqual(result, True)        
if __name__ == '__main__':
    unittest.main()