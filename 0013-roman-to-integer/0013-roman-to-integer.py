class Solution:
    def romanToInt(self, s: str) -> int:
        myDict = {}
        myDict["I"] = 1
        myDict["V"] = 5
        myDict["X"] = 10
        myDict["L"] = 50
        myDict["C"] = 100
        myDict["D"] = 500
        myDict["M"] = 1000
        newS = s[::-1]
        total = myDict[newS[0]]
        print(newS)
        for i in range(0, len(newS)-1):            
            if myDict[newS[i]] > myDict[newS[i+1]]:
                total = total - myDict[newS[i+1]]
                # print(total)
            elif myDict[newS[i]] <= myDict[newS[i+1]]:
                total = total + myDict[newS[i+1]]

        return total