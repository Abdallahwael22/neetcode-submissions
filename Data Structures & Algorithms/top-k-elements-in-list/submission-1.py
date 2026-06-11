class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for l in nums:
            freq[l]+=1
        
        sortedfreq=sorted(freq.items(),key=lambda item:item[1],reverse=True)
        sorteds=sortedfreq[:k]
        ss=[pair[0] for pair in sorteds]
        return ss
