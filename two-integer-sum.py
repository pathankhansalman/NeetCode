class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_idx = list(enumerate(nums))
        sorted_nums = list(sorted(nums_with_idx, key=lambda x: x[1]))
        i = 0
        j = len(sorted_nums) - 1
        while j > i:
            if sorted_nums[i][1] + sorted_nums[j][1] == target:
                return list(sorted([sorted_nums[i][0], sorted_nums[j][0]]))
            elif sorted_nums[i][1] + sorted_nums[j][1] > target:
                j -= 1
            else:
                i += 1
