class Solution:
    def isPalindrome(self, s):
        # code here
        low = 0
        high = len(s)-1
        
        
        def check(s, high, low):
            
            if (high - low + 1 <=1):
                return True
            
            if(s[low] != s[high]):
                return False

            
            return check(s,(high-1), (low+1))
        return check(s, high, low)

'''
Link: https://www.geeksforgeeks.org/problems/palindrome-string0817/1

Given a string s, find if it is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
Constraints:

1 ≤ s.size() ≤ 106
s consists only of lowercase English alphabets
'''