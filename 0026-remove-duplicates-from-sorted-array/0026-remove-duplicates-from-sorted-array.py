class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = len(nums)
        i = 0
        while i < len(nums):
            if i+1 == len(nums):
                # counter = counter + 1
                return counter
            
            if nums[i] == nums[i+1]:
                nums.pop(i)
                i = i-1
            i = i+1
        return counter