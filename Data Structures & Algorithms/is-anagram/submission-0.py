class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}

        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1

        for char in t:
            if char not in seen:
                return False
            seen[char] -= 1

        for val in seen.values():
            if val != 0:
                return False

        return True