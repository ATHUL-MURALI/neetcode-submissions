class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            preposition = target - num
            if preposition in seen:
                return [seen[preposition], i]
            seen[num] = i

        