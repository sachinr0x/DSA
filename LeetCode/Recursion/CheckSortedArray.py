class Solution:
    def isSorted(self, arr):
        # code here
        # for i in range(len(arr)-1):
        #     if arr[i] > arr[i+1]:
        #         return False
        # return True
        high = 1
        low = 0
        n = len(arr)
        def check(arr, low, high, n):
    
            if high >= n:
                return True
            
            if arr[low] > arr[high]:
                return False
            
            return check(arr, low+1, high+1, n)
        return check(arr, low, high, n)


'''
Link: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
Constraints:

1 ≤ arr.size() ≤ 106
-109 ≤ arr[i] ≤ 109
'''