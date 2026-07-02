class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        j = 0
        while len(nums) != len(res):
            num=1
            for i in range(len(nums)):
                if j != i:
                    num *= nums[i]
            res.append(num)
            j += 1
        return res