class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def back_track(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                back_track(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                back_track(openN, closedN + 1)
                stack.pop()

        back_track(0,0)
        return result