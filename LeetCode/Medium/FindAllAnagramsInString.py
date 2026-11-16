class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        low = 0
        high = 0
        res = []
        hmapp = {}
        hmaps = {}

        for char in p:
            hmapp[char] = hmapp.get(char, 0) + 1

        for high in range(len(s)):
            hmaps[s[high]] = hmaps.get(s[high], 0) + 1

            while (high - low + 1 > len(p)):
                hmaps[s[low]]  -= 1
                if hmaps[s[low]] == 0:
                    del hmaps[s[low]]
                low+=1

            if (all(hmaps.get(key) == value for key, value in hmapp.items())):
                res.append(low)

        return res


'''
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''