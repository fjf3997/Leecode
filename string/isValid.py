"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in dict:
                if len(stack) == 0 or dict[i] is not stack.pop():
                    return False
            else:
                stack.append(i)

        return len(stack) == 0
