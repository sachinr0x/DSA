class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hmaps1 = {}
        hmaps2 = {}
        counts1 = 0


        for char in s1:
            hmaps1[char] = hmaps1.get(char, 0) + 1
            counts1 +=1
    


        high = low = 0

        for high in range(len(s2)):
            hmaps2[s2[high]] = hmaps2.get(s2[high], 0) + 1

            while (high - low + 1) > counts1:
                hmaps2[s2[low]] -= 1
                if hmaps2[s2[low]] == 0:
                    del hmaps2[s2[low]]
                low+=1


            if all(hmaps2.get(key, 0) == value for key, value in hmaps1.items()):
                return True   
        
        return False

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''