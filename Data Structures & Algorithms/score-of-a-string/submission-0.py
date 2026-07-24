class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_vals = []
        
        for char in s:
            ascii_vals.append(int(ord(char)))
        
        score = 0
        for i in range(1, len(ascii_vals)):
            score += abs(ascii_vals[i] - ascii_vals[i - 1])

        return score