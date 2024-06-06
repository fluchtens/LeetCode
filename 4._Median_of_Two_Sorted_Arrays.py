from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_list: List[int] = []
        res: float = 0.0

        for nb in nums1:
            full_list.append(nb)
        for nb in nums2:
            full_list.append(nb)
        full_list.sort()

        list_size: int = len(full_list)
        if (list_size % 2 == 0):
            i1: int = int(list_size / 2) - 1
            i2: int = int(list_size / 2)
            res: float = (full_list[i1] + full_list[i2]) / 2
        else:
            i: int = int(list_size / 2)
            res = float(full_list[i])

        return res
