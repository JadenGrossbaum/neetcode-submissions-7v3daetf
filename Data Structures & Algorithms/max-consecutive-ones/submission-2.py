class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        curcount = 0
        for i in nums:
            if i == 1:
                curcount += 1
                if curcount > maxcount:
                    maxcount = curcount
            else:
                curcount = 0
        
        return maxcount
