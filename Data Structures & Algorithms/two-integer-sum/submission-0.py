class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     answer = {}

     for i,n in enumerate(nums):
        diff = target - n
        if diff in answer:
            return [answer[diff], i]
        answer[n] = i
