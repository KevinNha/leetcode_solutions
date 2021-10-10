'''
1) Read in and ignore any leading whitespace.
2) Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
    This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3) Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
4) Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
    Change the sign as necessary (from step 2).
5) If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
    Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6) Return the integer as the final result.
'''

import re

SIGNED_INTEGER_LOWER_LIMIT = -pow(2, 31)
SIGNED_INTEGER_UPPER_LIMIT = pow(2, 31) - 1

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        is_negative = False
        if s[0] in ['+', '-']:
            if s[0] == '-':
                is_negative = True
            s = s[1:]
        
        num = '0'
        for char in s:
            try:
                num = num + str(int(char))
            except:
                return self.get_return_num(is_negative, num)

        return self.get_return_num(is_negative, num)

    def get_return_num(self, is_negative, num):
        if is_negative:
            num = int(num) * -1
            if num < SIGNED_INTEGER_LOWER_LIMIT:
                return SIGNED_INTEGER_LOWER_LIMIT
            return num
        
        if int(num) > SIGNED_INTEGER_UPPER_LIMIT:
            return SIGNED_INTEGER_UPPER_LIMIT
        return int(num)

if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi(''))