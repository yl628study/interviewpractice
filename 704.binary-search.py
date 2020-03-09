#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or nums is None:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            mid = int(float(mid))
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1  
# @lc code=end

