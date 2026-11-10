import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        result = 0
        max_difference = sys.maxsize
        i=0

        for i in range (i, len(nums)-2, 1):

            left = i+1
            right = len(nums)-1

            while (left < right):

                sum = nums[i]+nums[left]+nums[right]

                if (sum == target):
                    return sum
                else:
                    difference = abs(sum - target)

                    if (difference < max_difference):
                        max_difference = difference
                        result = sum
                if (target < sum):
                    right -=1
                else:
                    left+=1       
        
        return result

    '''
    You are given an integer array nums of length n and an integer target.

Find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
    
    '''