class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            compl_num = target - num
            if compl_num in seen:
                return [seen[compl_num], idx]
            seen[num] = idx
