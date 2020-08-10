"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    
Note that an empty string is also considered valid.
"""
import collections

class Solution:
    def isValid(self, s: str) -> bool:
        paren_dic = {'(': ')', '{': '}', '[': ']'} # parentheses dictionary
        stack = collections.deque()
        for c in s:
            if c in paren_dic: 
                stack.append(c)
            elif not stack: 
                return False
            else:
                w = paren_dic[stack.pop()]
                if w != c:
                    return False
        return False if stack else True    
