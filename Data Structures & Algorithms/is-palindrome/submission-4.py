class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c for c in s if c.isalnum())
        s1 = s1.lower()
        left_pointer = 0
        right_pointer = len(s1) - 1
        if s1:
            while left_pointer <= right_pointer:
                if s1[left_pointer] == s1[right_pointer]:
                    left_pointer += 1
                    right_pointer -= 1
                else:
                    return False
            return True
        return True