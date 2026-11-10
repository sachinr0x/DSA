class Solution:
    def reverseString(self, s: str) -> str:
        # code here
        i = 0 
        
        s= list(s)
        
        left = 0
        right = len(s)
        
        while left < right:
            s[left], s[right-1] = s[right-1], s[left]
            
            left+=1
            right-=1
            
        return "".join(s)


    """
    Given a string s, reverse the string.

Examples:

Input: s = "Geeks"
Output: "skeeG"
Input: s = "for"
Output: "rof"
Input: s = "a"
Output: "a"
    """