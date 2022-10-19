class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            if target-v in nums[i+1:]:
                return [i, nums.index(target-v,i+1)]