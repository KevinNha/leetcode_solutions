from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort() # O n(log n)
        return_list = []
        for i in range(len(nums)): # O(n)
            target = 0 - nums[i]
            
            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                if nums[p1] + nums[p2] == target:
                    ans = [nums[i], nums[p1], nums[p2]]
                    ans.sort()
                    if ans not in return_list:
                        return_list.append(ans)
                    p2 -= 1
                elif nums[p1] + nums[p2] > target:
                    p2 -= 1
                else:
                    p1 += 1

        return return_list

if __name__ == "__main__":
    s = Solution()
    test_case1 = [-1,0,1,2,-1,-4]
    print(s.threeSum(test_case1))