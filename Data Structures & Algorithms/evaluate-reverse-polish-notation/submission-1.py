import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        previous_value = 0
        ops = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda a, b: int(a / b)
        }

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                right , left = stack.pop(), stack.pop()
                previous_value = ops[token](left, right)
                stack.append(previous_value)
        return stack[0]
