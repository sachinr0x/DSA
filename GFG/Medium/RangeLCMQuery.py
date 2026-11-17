import math

class Solution:
    def rangeLCMQuery(self, arr, queries):
        
        def lcm (arr, low, high):
            tempArr = arr[low:high+1]
            ans = 1
            for i in range (len(tempArr)):
                 ans = abs(ans * tempArr[i]) // math.gcd(ans, tempArr[i])
                
            return ans
        # code here
        res = []
        for query in queries:
                
                if query[0] == 1:
                    arr[query[1]] = query[2]
                    
                elif query[0] == 2:
                    j = query[1]
                    k = query[2]
                    
                    ans = lcm(arr, j, k)
                    
                    res.append(ans)
        
        return res

'''
Link: https://www.geeksforgeeks.org/problems/range-lcm-queries3348/1

Given an array arr[]  and a list of queries queries[][]. Each query can be one of the following two types:

Update Query: [1, index, value] --> Update the element at position index in the array to the given value.
Range Query: [2, L, R] --> Compute and return the Least Common Multiple (LCM) of all elements in the subarray from index L to R (inclusive).
Process all queries sequentially and return a list containing the results of all Type 2 queries.

Note: All operations follow 0-based indexing.

Examples :

Input: arr[] = [2, 3, 4, 6, 8, 16], queries[][] = [[2, 0, 2], [1, 3, 8], [2, 2, 5]]
Output: [12, 16]
Explanation: The queries are processed sequentially, updating the array when required.
[2, 0, 2]: LCM of [2, 3, 4] = 12
[1, 3, 8]: array becomes [2, 3, 4, 8, 8, 16]
[2, 2, 5]: LCM of [4, 8, 8, 16] = 16
Input: arr[] = [1, 2, 3, 4],  queries[][] = [[2, 0, 3], [1, 0, 5], [2, 0, 1]]
Output: [12, 10]
Explanation: The queries are processed sequentially, updating the array when required.
[2, 0, 3]: LCM of [1, 2, 3, 4] = 12
[1, 0, 5]: array becomes [5, 2, 3, 4]
[2, 0, 1]: LCM of [5, 2] = 10
Constraints:

1 ≤ arr.size(), arr[i] ≤ 104
1 ≤ queries.size() ≤ 105
0 ≤ L ≤ R ≤ arr.size() - 1
0 ≤ index ≤ arr.size() - 1
1 ≤ value ≤ 104
'''