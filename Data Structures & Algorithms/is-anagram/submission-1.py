class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sort = sorted(s)
        # t_sort = sorted(t)
        # if s_sort == t_sort:
        #     return True
        # return False

        s_seen = {}
        t_seen = {}
        for char in s:
            if char in s_seen:
                s_seen[char] = s_seen[char] + 1
            else:
                s_seen[char] = 1
                        
        for char in t:
            if char in t_seen:
                t_seen[char] = t_seen[char] + 1
            else:
                t_seen[char] = 1
        
        return True if s_seen == t_seen else False
                        