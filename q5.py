class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (1, s[0])

        if len(s) == 1:
            return s
        for index, letter in enumerate(s):
            left_position = index - 1
            right_position = index + 1
            palindrome_length = 1
            palindrome_pattern = letter
            while left_position >= 0 and right_position < len(s):
                if s[left_position] == s[right_position]:
                    palindrome_length += 2
                    palindrome_pattern = s[left_position] + palindrome_pattern + s[left_position]
                    if palindrome_length > longest[0]:
                        longest = (palindrome_length, palindrome_pattern)
                    left_position -= 1
                    right_position += 1
                else:
                    break

            left_position = index - 1
            right_position = index + 1
            palindrome_length = 1
            palindrome_pattern = letter

            if right_position < len(s) and s[right_position] == letter:
                palindrome_length = 2
                palindrome_pattern = letter + letter
                if palindrome_length > longest[0]:
                    longest = (palindrome_length, palindrome_pattern)
                right_position += 1
            
            while left_position >= 0 and right_position < len(s):
                if s[left_position] == s[right_position]:
                    palindrome_length += 2
                    palindrome_pattern = s[left_position] + palindrome_pattern + s[left_position]
                    if palindrome_length > longest[0]:
                        longest = (palindrome_length, palindrome_pattern)
                    left_position -= 1
                    right_position += 1
                else:
                    break
        return longest[1]
        
# Need to figure out whether palindrome or not first
# Check if it can go left or not
# Each letter basically needs to check through two possibilities:
#   1. using the letter as the center point
#   2. using the letter and the right letter as the center point
# baaabb