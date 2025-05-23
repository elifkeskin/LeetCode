class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    # The question asks us to understand if an array has another array subset.
    # Here, subsequence means preserving the order of a character without changing it, by removing some of the characters from between.
        S = len(s)
        T = len(t)

        if S == 0:
            return True
        if S > T:
            return False

        j = 0
        for i in range(T):
            if j < S and t[i] == s[j]:
                j += 1
                if j == S:
                    return True
        return False


    # Time: O(T) =>  We run it for the length of the array T.
    # Space: O(1) =>  we did not use any extra space.(There is no extra data structure.)
