class Solution:
    def countTriplets(self, sum, arr):
        
        res_count = 0
        i=0
        arr.sort()
        
        for i in range(i, len(arr)-2, 1):
            
            left = i+1
            right = len(arr)-1
            
            while(left<right):
                
                triplet_sum = arr[i]+arr[left]+arr[right]
                
                if (triplet_sum < sum):
                    res_count += (right-left)
                    left+=1
                else:
                    right-=1
                   
        return res_count
                
        '''
        Given an array arr[] of distinct integers and an integer sum, count the number of unique triplets of elements whose sum is strictly less than sum. A triplet is identified only by the three elements it contains, so different permutations of the same three elements are counted as one triplet.

Examples :

Input: sum = 2, arr[] = [-2, 0, 1, 3]
Output:  2
Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3). 
Input: sum = 12, arr[] = [5, 1, 3, 4, 7]
Output: 4
Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).
Constraints:

1 ≤ sum ≤ 105
3 ≤ arr.size() ≤ 103
-103 ≤ arr[i] ≤ 103
        '''