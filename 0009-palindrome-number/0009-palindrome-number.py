class Solution:
    def isPalindrome(self, x: int) -> bool:
      x = str(x)
      y = x[::-1]
      print(x)
      print(y)
      if y==x:
         return True
      else:
         return False