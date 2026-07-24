class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr) - 1:
            greatest = arr[i + 1]
            j = i + 1
            while j < len(arr):
                greatest = max(arr[j], greatest)
                j += 1
            arr[i] = greatest
            i += 1
        arr[-1] = -1
        return arr