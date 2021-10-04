class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pattern = ''
        max_len = len(longest_pattern)
        for i in range(len(s)):
            remaining_s = s[i:]
            if len(longest_pattern) > len(remaining_s):
                return longest_pattern
            
            while len(remaining_s) >= 1:
                if remaining_s == remaining_s[::-1]:
                    if len(remaining_s) > max_len:
                        max_len = len(remaining_s)
                        longest_pattern = remaining_s
                    break
                else:
                    remaining_s = s[:-1]
        return longest_pattern