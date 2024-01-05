class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        hours.reverse()
        emp = 0
        for n in hours:
            if n >= target:
                emp = emp +1
            else:
                return emp
        return emp
        
        