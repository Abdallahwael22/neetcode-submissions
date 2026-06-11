class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l_sub=[]
        l_all=[]
        flag=0
        for stg in strs:
            print(f"stg: {stg}")
            for st in strs:
                print(f"st : {st}")
                if(sorted(st)==sorted(stg)):
                    l_sub.append(st)
            strs=[x for x in strs if x not in l_sub]
            if len(l_sub)>0:
                l_all.append(l_sub)
            l_sub=[]
        return l_all