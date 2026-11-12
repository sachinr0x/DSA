class Solution:
    def countDigits(self, n: int) -> int:
        # Code here        
        numStr = str(n)
        
        return len(numStr)


'''
Given a number n, return the count of digits in this number.

Examples :

Input: n = 1567
Output: 4
Explanation: There are 4 digits in 1567, which are 1, 5, 6 and 7.
Input: n = 99999
Output: 5
Explanation: The number of digits in 99999 is 5.
Constraints:

0 ≤ n ≤ 231 -1
'''