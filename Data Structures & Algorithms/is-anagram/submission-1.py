class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26

        for i, s_char in enumerate(s):
            t_char = t[i]

            counts[ord(s_char) - ord("a")] += 1
            counts[ord(t_char) - ord("a")] -= 1
        
        return not any(counts)