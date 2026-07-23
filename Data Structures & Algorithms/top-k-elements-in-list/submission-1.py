class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
            
        result = sorted(freq, key=freq.get, reverse=True)[:k]
        return result