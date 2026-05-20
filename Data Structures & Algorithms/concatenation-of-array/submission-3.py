class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = []
        n = len(nums)
        for i in range(n*2):
            if i < n:
                new_arr.append(nums[i])
            else:
                new_arr.append(nums[i%n])
        
        return new_arr

