class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            if (num - 1) not in numSet:
                x = num + 1
                while (x in numSet):
                    x += 1
                longest = max(longest, x - num)

        return longest 