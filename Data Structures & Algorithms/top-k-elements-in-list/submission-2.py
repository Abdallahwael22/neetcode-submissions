import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        out=[]
        for l in nums:
            freq[l]+=1
        l=[[] for i in range(len(nums)+1)]
        for key,v in freq.items():
            l[v].append(key)
        for i in range(len(l)-1,0,-1):
            for n in l[i]:
                out.append(n)
                if len(out)==k:
                    return out
                    
                
