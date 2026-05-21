class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
                return True
        
        return False
