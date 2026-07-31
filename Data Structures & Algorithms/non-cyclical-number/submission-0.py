class Solution:
    def isHappy(self, n: int) -> bool:
        hashset=set()
        
        while n not in hashset:
            hashset.add(n)
            n=self.square(n)
            if n==1:
                return True
        return False

    def square(self,n):
        output=0
        while n:
            inter=n%10
            output+=inter**2
            n=n // 10
        return output