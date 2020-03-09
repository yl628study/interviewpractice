#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
def binary_search(nums, target):
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
    return None

result = binary_search([1,2,3,4,6], 4)
print(result)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
# @lc code=end

