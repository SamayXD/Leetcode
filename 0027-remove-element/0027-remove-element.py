class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        myNums = nums
        lateNums = []
        # for n in range(len(myNums)-1):
        #     if myNums[n] == val:
        #         lateNums.append(val)
        #         myNums.remove(val)
        #         print(myNums)
        
        while val in myNums:
            myNums.remove(val)
            lateNums.append(val)
            

        k = len(myNums)
        myNums = myNums + lateNums
        nums = myNums

        return k