from datetime import datetime

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        current_row = 0
        zigzag = self.initialize_zigzag(numRows)
        row_going_up = True
        for i in range(len(s)):
            zigzag.get(current_row).append(s[i])
            if row_going_up:
                current_row += 1
            else:
                current_row -= 1
            row_going_up = self.get_direction(current_row, numRows, row_going_up)

        return_string = ''
        for row in zigzag.values():
            return_string += ''.join(row)

        return return_string

    def get_direction(self, current_row, num_rows, row_going_up):
        if row_going_up and current_row == num_rows -1:
            return False
        elif row_going_up and current_row < num_rows:
            return True
        elif (not row_going_up) and current_row <= 0:
            return True
        else:
            return False

    def initialize_zigzag(self, num_rows) -> dict:
        zigzag = {}
        for i in range(num_rows):
            zigzag.setdefault(i, [])
        return zigzag

if __name__ == '__main__':
    solution = Solution()
    before = datetime.now()
    print(solution.convert('AB', 1))
    after = datetime.now()
    print("Function execution time: ", after - before)