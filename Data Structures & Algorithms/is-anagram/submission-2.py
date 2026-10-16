class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for n, m in zip(s, t):
            if n in s_dict:
                s_dict[n] += 1
            else:
                s_dict[n] = 1
            if m in t_dict:
                t_dict[m] += 1
            else:
                t_dict[m] = 1
        return s_dict == t_dict
        