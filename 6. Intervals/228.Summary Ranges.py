class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
     # If the range consists of a single number, write the number directly. If the range contains more than one number and is consecutive, express the starting and ending numbers in the same format as starting and ending.
     # Example 1:   nums = [0,1,2,4,5,7] 
    # [0,2] --> "0->2"
    # [4,5] --> "4->5"
    # [7,7] --> "7"
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]
            # Consecutive numbers are checked (nums[i] + 1 == nums[i + 1])
            while i < len(nums)-1 and nums[i] + 1 == nums[i+1]:
                i += 1

           # If start is different, there is a range of numbers.
            if start != nums[i]:
                ans.append(str(start)+ "->" + str(nums[i]))
            else:
                ans.append(str(nums[i]))
            
            i += 1
        return ans
    
    # Time: O(n) because we iterate through the array once.
    # Space: O(n) because we store the result in a list.
