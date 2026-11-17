class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open = close = 0
        temp = []
        res = []


        def parent(open, close, temp, res, n):

            if (open == n and close == n):
                res.append(''.join(temp))
                return

            #open
            if (open < n):
                temp.append("(")
                parent(open+1, close, temp, res, n)
                temp.pop()

            #close
            if ( close < open):
                temp.append(")")
                parent(open, close+1, temp, res, n)
                temp.pop()

        parent(open, close, temp, res, n)
        return res  

'''
Link: https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''