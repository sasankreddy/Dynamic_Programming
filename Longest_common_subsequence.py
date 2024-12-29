class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        My approach:
        - The problem is about finding the longest subsequence that is common in both strings `text1` and `text2`.
        - A subsequence is a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
        - To solve this using Dynamic Programming (DP), we'll build a 2D DP table where `dp[i][j]` represents the length of the longest common subsequence between the first `i` characters of `text1` and the first `j` characters of `text2`.
        
        Steps:
        1. Initialize a 2D DP table `dp` of size `(n+1) x (m+1)`, where `n` and `m` are the lengths of `text1` and `text2`, respectively. Set all values to 0.
        2. Traverse through both strings using two loops: the outer loop iterating through `text1` and the inner loop iterating through `text2`.
        3. If the characters `text1[i-1]` and `text2[j-1]` match, set `dp[i][j] = dp[i-1][j-1] + 1` (because we have found one more character in the common subsequence).
        4. If they do not match, set `dp[i][j] = max(dp[i-1][j], dp[i][j-1])` (the longest subsequence would be the maximum of excluding either the character from `text1` or `text2`).
        5. Finally, return `dp[n][m]`, which will contain the length of the longest common subsequence.
        
        Time Complexity: O(n * m), where `n` and `m` are the lengths of `text1` and `text2`. We fill the DP table of size `(n+1) x (m+1)`, each entry takes constant time.
        Space Complexity: O(n * m), for storing the DP table.
        """
        
        n, m = len(text1), len(text2)
        # Initialize a DP table with dimensions (n+1) x (m+1) and all values set to 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:  # If characters match
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  # If characters don't match, take the maximum of excluding one character from either string
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the longest common subsequence is stored in dp[n][m]
        return dp[n][m]
