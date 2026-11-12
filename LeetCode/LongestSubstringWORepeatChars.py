class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        high = low = 0
        hmap = {}

        for high in range(len(s)):
            hmap[s[high]] = hmap.get(s[high],0) + 1

            while hmap[s[high]] > 1:
                hmap[s[low]] = hmap.get(s[low]) - 1
                if hmap.get(s[low]) == 0:
                    del hmap[s[low]]
                low+=1        
        
            winSize = high - low + 1
            res = max(res, winSize)

        return res

'''
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
'''