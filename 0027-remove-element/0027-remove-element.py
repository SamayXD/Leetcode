class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lateNums = []
        
        while val in nums:
            nums.remove(val)
            lateNums.append(val)
            
        k = len(nums)
        nums = nums + lateNums

        return k