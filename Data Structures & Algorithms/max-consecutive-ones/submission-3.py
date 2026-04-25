class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount, curcount = 0, 0
        for i in nums:
            if i == 0:
                maxcount = max(maxcount, curcount)
                curcount = 0
            else:
                curcount += 1
        
        return max(curcount, maxcount)
