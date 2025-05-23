class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    # We are asked to find the longest common prefix among words in a series.  If there is no common prefix between these words, we are asked to return an empty string.

         min_length = float('inf')

        # The common prefix cannot exceed the shortest word.
         for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        
         i = 0
         while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
         return strs[0][:i]

        # Time: O(n*m) => n = length of string, m=the shortest word length
        # Space: O(1) => we did not use any extra space.(There is no extra data structure.)
        
        
   

