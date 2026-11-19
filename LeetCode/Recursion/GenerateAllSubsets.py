class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        diary = []

        idx = 0
        n = len(nums)

        def sub(ans, diary, idx, n, nums):

            if (idx == n):
                temp = []
                for i in range(len(diary)):
                    temp.append(diary[i])
                ans.append(temp)
                return

                    
            sub(ans, diary, idx+1, n, nums)

            diary.append(nums[idx])

            sub(ans,diary, idx+1, n, nums)
            diary.pop()
        
        sub(ans,diary, idx, n, nums)
        return ans

'''
Link: https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''