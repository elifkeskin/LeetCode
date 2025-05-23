class Solution:
    def findMin(self, nums: List[int]) -> int:
# In this question, the array is starting from the minimum element to rotate.
# The array is sorted from smallest to largest starting from the break point.
        left, right = 0, len(nums) - 1
                
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # minimum on the right
                left = mid + 1
            else:
                # Minimum on the left or mid
                right = mid
                
        return nums[left]


# Time Complexity : O(logn) =>Binary Search splits an array in half at each step.
# So the number of operations increases logarithmically.
# Space Complexity: O(1) => O(1) because we did not use any extra space.(There is no extra data structure.)
