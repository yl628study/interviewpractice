#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        def findPosition(situation):
            left = 0
            right = len(nums) - 1
            position = -1
            while left + 1 < right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                elif(situation == 'first'):
                    right = mid
                else:
                    left = mid
            if situation == 'first':        
                if nums[left] == target:
                    position = left
                elif nums[right] ==  target:
                    position = right
            if situation == 'last':        
                if nums[right] == target:
                    position = right
                elif nums[left] ==  target:
                    position = left
            return position

        first = findPosition('first')
        last = findPosition('last')
        return [first, last]

    
# @lc code=end

