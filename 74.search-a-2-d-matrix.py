#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col =  len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            midIndex = (left + right) // 2
            midValue = matrix[midIndex // col][midIndex % col]
            if target < midValue:
                right = midIndex - 1
            elif target > midValue:
                left = midIndex + 1
            else:
                return True

        return False

# @lc code=end

