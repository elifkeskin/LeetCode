
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}  # number -> index

        for i in range(len(nums)):
            difference = target - nums[i]  # if target = 7 and list = [10, 2, 4, 5, 8] then difference= 10 -7
            if difference in num_dict:
                return [num_dict[difference], i]
            num_dict[nums[i]] = i

 # Time Complexity: O(n) because we used one for loop. (n input == n output )
 # Space Complexity: O(n) because we used one extra dictionary.