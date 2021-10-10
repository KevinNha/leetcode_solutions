SIGNED_INTEGER_LOWER_LIMIT = -pow(2, 31)
SIGNED_INTEGER_UPPER_LIMIT = pow(2, 31) - 1

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        is_negative = False
        if x < 0:
            is_negative = True
            x = x * -1
        
        int_as_str = str(x)
        int_as_list = [num for num in int_as_str]

        int_reversed = int_as_list[::-1]
        reversed_int_as_str = ''.join(int_reversed)
        reversed_int = int(reversed_int_as_str)
        if is_negative:
            reversed_int = reversed_int * -1

        if reversed_int > SIGNED_INTEGER_UPPER_LIMIT or reversed_int < SIGNED_INTEGER_LOWER_LIMIT:
            return 0
            
        return reversed_int

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))