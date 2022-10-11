#Ques: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            if height[left] > height[right]: #according to the shown picture in example
                min_height = height[right]
                min_pointer = right
            else:
                min_height = height[left]
                min_pointer = left
            max_area = (right - left) * min_height #width *height
            area = max(area, max_area)
            if left == min_pointer:
                left += 1
            if right == min_pointer:
                right -=1
    
        return area 

        #TC: O(n) SC: O(1)
        