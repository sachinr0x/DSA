class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        high = low = 0
        res = 0
        hmap = {}

        for high in range(len(s)):
            hmap[s[high]] = hmap.get(s[high],0)+1

            winSize = high - low + 1
            diff = winSize - max(hmap.values())

            while (diff > k):
                hmap[s[low]] = hmap.get(s[low],0) - 1
                if(hmap.get(s[low]) == 0):
                    del hmap[s[low]]
                low+=1
                winSize = high - low + 1
                diff = winSize - max(hmap.values())
                
            winSize = high - low + 1
            res = max(winSize, res)

        return res
        
'''
Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''