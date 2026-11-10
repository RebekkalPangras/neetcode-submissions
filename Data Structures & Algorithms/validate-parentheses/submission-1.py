class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in pairs:
                # If stack is empty or top doesn't match, it's invalid
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
                
        return not stack
