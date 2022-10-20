class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        production = reduce(lambda x, y: x * y, nums)
        answer = []
        for num in nums:
            if num != 0:
                answer.append(production//num)
            else:
                nums_z = nums[:]
                nums_z.remove(num)
                new = reduce(lambda x, y: x * y, nums_z)
                answer.append(new)
        return answer
        