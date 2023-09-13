from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: List[int] = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)

        return (result)

if __name__ == "__main__":
    solution = Solution()

    nums: List[int] = [7, 2, 11, 15]
    target: int = 9
    print(solution.twoSum(nums, target))
