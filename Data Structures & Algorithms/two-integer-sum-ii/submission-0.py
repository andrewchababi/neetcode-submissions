class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftP = 0
        rightP = len(numbers) -1

        while leftP < rightP:
            current_sum = numbers[leftP] + numbers[rightP]
            if current_sum > target:
                rightP -= 1 
            elif current_sum < target:
                leftP += 1
            elif current_sum == target:
                return [leftP + 1, rightP + 1]
    