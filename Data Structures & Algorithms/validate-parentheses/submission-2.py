class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []
        for c in s:
            if c in hash_map.values():
                stack.append(c)
                
            if c in hash_map.keys():
                if not stack or hash_map[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
            
        return not stack

