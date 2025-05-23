class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We are asked to return an array containing the product of every element in an array except the current element. 
        # Example 1: nums = [1,2,3,4] =>exclude of 2 => 1 * 3 * 4 = 12
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):
            j = -i -1   # j represents the sequence starting from the end and proceeding towards the beginning.
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [l*r for l,r in zip(l_arr, r_arr)]

# Time Complexity: O(n) =>  because we used one for loop. (n input == n output )
# Space Complexity : O(n) => we used two arrays of size n.
