class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        posList = []
        negList = []

        for i in range(len(nums)):
            if (nums[i] < 0):
                negList.append(nums[i])
            else:
                posList.append(nums[i])

        if (len(negList) == 0):
            for i in range(len(posList)):
                posList[i] = posList[i]**2
            return posList
        elif (len(posList) == 0):
            for i in range(len(negList)):
                negList[i] = negList[i]**2
            negList.reverse()
            return negList

        p=q=0    

        for p in range(len(posList)):
                posList[p] = posList[p]**2
        for q in range(len(negList)):
                negList[q] = negList[q]**2
        negList.reverse()
    
        i=j=0
        res = []

        while( i < len(posList) and j < len(negList) ):

            if (posList[i] <= negList[j]):
                res.append(posList[i])
                i+=1
            else:
                res.append(negList[j])
                j+=1

        while (j < len(negList)):
            res.append(negList[j])
            j+=1
        while (i< len(posList)):
            res.append(posList[i])
            i+=1
        return res

        # for i in range(len(nums)):
        #     nums[i] = nums[i]**2

        # nums.sort()
        # return nums

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''