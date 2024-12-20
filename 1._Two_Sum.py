from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i: int = 0
        while (i < len(nums)):
            j: int = i + 1
            while (j < len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
                j = j + 1
            i = i + 1
        return 0

# test
