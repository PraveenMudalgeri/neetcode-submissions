class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
            print(f'j : {j}')
        print(f'len(t): {len(t)}, j: {j}')
        return len(t) - j