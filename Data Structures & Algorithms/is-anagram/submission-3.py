class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}
        for i in s:
            if i in seen1:
                seen1[i] += 1
            else:
                seen1[i] = 1

        for i in t:
            if i in seen2:
                seen2[i] += 1
            else:
                seen2[i] = 1
        
        if seen1 == seen2:
            return True
        else:
            return False
        
        