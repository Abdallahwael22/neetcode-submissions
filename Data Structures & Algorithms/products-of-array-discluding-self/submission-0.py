class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        productList=[]
        i=0
        x=0
        while (i< len(nums)):
            while(x<len(nums)):
                if (x==i):
                    x+=1
                    continue
                product*=nums[x]
                x+=1
            productList.append(product)
            product=1
            x=0
            i+=1
        return productList