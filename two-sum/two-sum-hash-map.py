from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i


print(Solution().twoSum([2,7,11,15], 9))
