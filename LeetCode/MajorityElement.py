class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurances = dict({})

        for num in nums:
            occurances[num] = occurances.get(num,0) +1
        
        max_occurance = max(occurances, key = occurances.get)
        print(occurances)

        return max_occurance


'''
Note:
d = {
    10: 50,
    20: 100,
    30: 75
}

print(max(d)) #30
print(max(d, key=d.get)) #20
print(max(d.values())) #100

my_dict = {1: 100}

print(my_dict[2])       # KeyError
print(my_dict.get(2))   # None
print(my_dict.get(2, 0)) # 0

my_dict[2] raises an error if the key doesn't exist.
my_dict.get(2) returns None if the key doesn't exist.
my_dict.get(2, 0) returns 0 if the key doesn't exist.

max(d) → finds the maximum key.
max(d, key=d.get) → finds the key whose value is maximum.
d.get → retrieves the value associated with a key.

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''