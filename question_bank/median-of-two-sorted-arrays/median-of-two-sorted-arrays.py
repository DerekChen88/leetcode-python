# -*- coding: utf-8 -*-
# @Author  : LG

"""
执行用时：80 ms, 在所有 Python3 提交中击败了8.29% 的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了6.15% 的用户

解题思路：
    先比较两列表的最小值
    1. 从最小值较小的列表中，寻找比最小值较大列表最小值 小的值。
    2. 对最小值较小列表中剩下的值
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if nums1 == [] or nums2 == []:
            l = nums1
            l.extend(nums2)
            num = len(l)
            if num %2 == 0:
                media = (l[num//2-1] + l[num//2])/2
            else:
                media = l[num//2]
            return media

        if min(nums1) <= min(nums2):
            min_l, max_l = nums1, nums2
        else:
            min_l, max_l = nums2, nums1

        r = self.search(min(max_l), min_l)
        num = len(nums1) + len(nums2)
        p, q = 0, 0
        l = min_l[:r]
        min_l = min_l[r:]

        while r <= num//2:
            if min_l == [] or max_l == []:
                l.extend(min_l)
                l.extend(max_l)
                break
            if min_l[0] < max_l[0]:
                l.append(min_l.pop(0))
            else:
                l.append(max_l.pop(0))

        if num %2 == 0:
            media = (l[num//2-1] + l[num//2])/2
        else:
            media = l[num//2]
        return media

    def search(self, num, nums):
        r = 0
        if num < max(nums):
            while num > nums[r]:
                r += 1
            return r
        else:
            return len(nums)-1