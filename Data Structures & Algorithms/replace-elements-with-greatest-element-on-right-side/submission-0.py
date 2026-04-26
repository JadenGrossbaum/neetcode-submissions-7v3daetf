class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = []
        i = 0
        while i < len(arr)-1:
            ge_on_right = max(arr[i+1:])
            output.append(ge_on_right)
            i += 1
        output.append(-1)

        return output