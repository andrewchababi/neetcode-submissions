class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                stackInd, stackVal = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((i, v))
        return result