class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l={}
        for i,num in enumerate (nums):
            comp=target-num
            if comp in l:
                return[l[comp],i]
            l[num]=i
        return [0,0]