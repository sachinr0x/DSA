import sys
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        high = low = 0
        minLen = sys.maxsize
        res = ""
        hmapt = {}
        hmaps = {}

        for i in range(len(t)):
            hmapt[t[i]] = hmapt.get(t[i],0) + 1

        for high in range(len(s)):
            hmaps[s[high]] = hmaps.get(s[high],0) + 1

            while all(hmaps.get(key, 0) >= value for key,value in hmapt.items()):
                winSize = high - low + 1
                if winSize < minLen:
                    minLen = winSize
                    res = s[low:high+1]

                hmaps[s[low]] -= 1
                if hmaps[s[low]] == 0:
                    del hmaps[s[low]]
                low+=1
                
        return res
            
                

'''
Link: https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''