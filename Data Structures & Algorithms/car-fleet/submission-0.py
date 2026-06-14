class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        merged = list(tuple(zip(position, speed)))
        merged.sort(reverse= True)
        for pos, speed in merged:
            t = (target - pos)/speed
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
