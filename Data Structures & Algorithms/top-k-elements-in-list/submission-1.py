class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countofNums = {}
        for num in nums:
            countofNums[num] = countofNums.get(num, 0) + 1

        sorted_items = sorted(countofNums.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])

        return result