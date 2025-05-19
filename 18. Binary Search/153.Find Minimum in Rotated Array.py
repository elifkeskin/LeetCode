class Solution:
    def findMin(self, nums: List[int]) -> int:
# In this question, the array is starting from the minimum element to rotate.
# The array is sorted from smallest to largest starting from the break point.
        minn = float('inf') #infinitive 
        for num in nums:
            if num < minn:
                minn = num
        return minn

# Time Complexity : O(n) => O(n) because we used one for loop. (n input == n output )
# Space Complexity: O(1) => O(1) because we did not use any extra space.(There is no extra data structure.)
# Optimization Method: Recursive Binary Search
