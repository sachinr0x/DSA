class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mobile = {"2": "abc", "3":"def" , "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",}
        res = []
        idx = 0
        diary = []
        n = len(digits)

        def sol(res, idx, diary, digits, n, mobile):

            #baseCase
            if (idx == n):
                res.append(''.join(diary))
                return

            choice = mobile[digits[idx]]

            for i in range(len(choice)):
                diary.append(choice[i])
                sol(res, idx+1, diary, digits, n, mobile)
                diary.pop()
            return
        sol(res, idx, diary, digits,n, mobile )
        return res

'''
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

[TAKE REFERENCE OF IMAGE FROM QUESTION LINK]
 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''