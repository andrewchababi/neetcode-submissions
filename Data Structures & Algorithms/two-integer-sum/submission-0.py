class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in hash_map:
                return [hash_map[compliment], i]
            hash_map[num] = i

        return []