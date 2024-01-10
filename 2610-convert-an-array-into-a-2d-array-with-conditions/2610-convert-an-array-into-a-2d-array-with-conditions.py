class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []
        
        for n in nums:
            rows = count[n]
            if len(res) == rows:
                res.append([])
            
            res[rows].append(n)
            count[n] += 1
        return res