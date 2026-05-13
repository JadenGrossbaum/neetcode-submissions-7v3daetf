class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0
        result = 0
        for i in range(len(operations)):
            if operations[i] == '+':
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operations[i]))

        for i in stack:
            result += i
        
        return result