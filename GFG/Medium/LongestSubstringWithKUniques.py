class Solution:
    def longestKSubstr(self, s, k):
        # code here
        
        hmap= {}
        resCount = -1
        high = low = 0
        
        
        for high in range (len(s)):
            
            hmap[s[high]] = hmap.get(s[high], 0) + 1
            
            while (len(hmap) > k):
                hmap[s[low]] = hmap.get(s[low]) - 1
                
                if hmap.get(s[low]) == 0:
                    del hmap[s[low]]
                low+=1
            if len(hmap) == k:
                winSize = high - low + 1
                resCount = max(winSize, resCount)
            
        
        return resCount

'''
Link: https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1. 

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.
Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
Constraints:

1 ≤ s.size() ≤ 105
1 ≤ k ≤ 26
'''