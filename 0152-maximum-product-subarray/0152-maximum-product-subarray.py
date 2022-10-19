class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -(10*2*10**4)
        local_max_product = 1
        min_product = 10*2*10**4
        local_min_product = 1
        for i in range(len(nums)):
            if nums[i]<0:
                local_max_product, local_min_product = local_min_product, local_max_product
            local_max_product = max(local_max_product*nums[i], nums[i])
            local_min_product = min(local_min_product*nums[i], nums[i])
            max_product = max(local_max_product, max_product)
            min_product = min(local_min_product, min_product)

        return max_product

            