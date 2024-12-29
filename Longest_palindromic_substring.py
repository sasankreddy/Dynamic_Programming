class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        My approach:
        - The problem is to find the longest palindromic substring in the given string `s`.
        - A substring is a continuous segment of the string.
        - A palindrome is a string that reads the same forward and backward.
        - The approach involves iterating through all possible substrings of `s` and checking if they are palindromic.
        - For each substring `s[i:j+1]`:
            - Check if it is a palindrome by comparing it with its reverse.
            - If it is longer than the current longest palindrome, update the `Max_Len` and `Max_Str`.
        - Return the longest palindromic substring.

        Time Complexity: O(n^3), where `n` is the length of `s`.
        - Generating all substrings takes O(n^2).
        - Checking if each substring is a palindrome takes O(n).
        Space Complexity: O(1), as no additional data structures are used.
        """
        if len(s) <= 1:
            return s  # If the string has 0 or 1 characters, it is already a palindrome.

        Max_Len = 1  # Maximum length of palindrome found so far.
        Max_Str = s[0]  # Longest palindromic substring found so far.

        # Iterate through all substrings
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                # Check if the substring is palindromic and longer than the current longest palindrome
                if j - i + 1 > Max_Len and s[i:j + 1] == s[i:j + 1][::-1]:
                    Max_Len = j - i + 1
                    Max_Str = s[i:j + 1]

        return Max_Str
