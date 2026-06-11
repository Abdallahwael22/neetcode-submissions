class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        prefix=[1]
        i=0
        while (i<len(nums)):
            product*=nums[i]
            prefix.append(product)
            i+=1
        i=len(nums)-1
        product=1
        suffix=[1]
        while (i>-1):
            product*=nums[i]
            suffix.append(product)
            i-=1
        products=[]
        i=0
        while(i<len(nums)):
            product=prefix[i]*suffix[len(nums)-(i+1)]
            products.append(product)
            i+=1
        return products
