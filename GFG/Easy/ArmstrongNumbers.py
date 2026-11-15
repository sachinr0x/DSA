class Solution:
    def armstrongNumber(self, n: int) -> bool:
        
        # code here
        string = str(n)
        
        arr = [int(x) ** len(string) for x in string]
        sum = 0
        
        for i in arr:
            sum+= i
            
        if n == sum:
            return True
        
        return False


'''
Link: https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
Given a positive integer n, determine whether it is an Armstrong number or not.

An Armstrong number is a number where, sum of each digit raised to the power digit count, is equal to the original number.

Examples:

Input: n = 153
Output: true
Explanation: 13 + 53 + 33 = 153, which is equal to the original number.
Input: n = 1634
Output: true
Explanation: 14 + 64 + 34 + 44 = 1634, which is equal to the original number.
Input: n = 100
Output: false
Explanation: 13 + 03 + 03 = 1, which is not equal to 100.
Constraints:

1 ≤ n < 106

'''