class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        summ = 0
        n = len(s)
        i = 0

        while i < n:
            # If counter i is not at the last character and the value of the current character is less than the value of the next character
            if i < n-1 and d[s[i]] < d[s[i+1]]: # Ex: IV
                summ += d[s[i+1]] - d[s[i]]  # IV = V - I 
                i += 2  # 2 character is completed.
            else:
                summ += d[s[i]]
                i += 1  # 1 character is completed.
        return summ
    
 # Time: O(n) => n = length of string
 # Space : O(n) => d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} => There is only a fixed size dictionary in the code