class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False       
       
       
       
       
       
       
       
       
       
       
       
       
       
       # if(len(nums)==len(set(nums))):
        #   return False
        #else:
         #   return True 
