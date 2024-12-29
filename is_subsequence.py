class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        My approach:
        - The problem asks to determine if string `s` is a subsequence of string `t`.
        - A subsequence means all characters of `s` appear in `t` in the same order, but not necessarily consecutively.
        - Use two pointers (`i` for `s` and `j` for `t`) to traverse both strings.
        - Start both pointers at the beginning:
            - If characters at `s[i]` and `t[j]` match, move both pointers.
            - Otherwise, move only `j` (to continue checking `t` for potential matches).
        - If `i` reaches the end of `s`, it means all characters of `s` were found in `t` in the correct order.

        Time Complexity: O(n), where n is the length of `t`.
        - Each character in `t` is checked at most once.
        Space Complexity: O(1), as no extra space is used.
        """
        i = 0  # Pointer for `s`
        j = 0  # Pointer for `t`

        # Traverse both strings
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move `i` only if characters match
            j += 1  # Always move `j`

        # If all characters of `s` are matched, `i` should reach the end of `s`
        return i == len(s)
