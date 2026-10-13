class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Questions
        1. What if both empty strings?


        Approaches
        1. Brute-force
           > O(len(s) * len(t)) time & O(max(len(s), len(t))) space
        - make a copy of s or t
        - for each s_char in s:
        -- for each t_char in t:
        --- check and mark somehow
        2. Sorting
        - sort both strings and check if they are the same
        - Let n be len(s); m be len(t); 
        - > O(n log n + m log m + min(n, m)) time
            & O(max(n, m)) space
        3. Counter dict
        - have char to # occurences dicts for both
        - compare both dicts and check if they are the same
        - > O(max(n, m)) time & O(max(n, m)) space
        """

        """
              v
        s = "jar", t = "jam"

        s_chars_to_counts = {
            "j": 1,
            "a": 1,
            "r": 1
        }

        s_chars_to_counts = {
            "j": 1,
            "a": 1,
            "m": 1
        }
        """
        
        s_chars_to_counts, t_chars_to_counts = {}, {}

        for s_char in s:
            if s_char in s_chars_to_counts:
                s_chars_to_counts[s_char] += 1
            else:
                s_chars_to_counts[s_char] = 1
        
        for t_char in t:
            if t_char in t_chars_to_counts:
                t_chars_to_counts[t_char] += 1
            else:
                t_chars_to_counts[t_char] = 1
        
        return s_chars_to_counts == t_chars_to_counts