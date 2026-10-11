class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Questions
        1. Guarnanteed that nums only contains ints
        2. Edge cases: what if len(nums) == 0 or 1

        Let n = len(nums)

        Approaches
        1. Brute-force: using 2 loops
           - time: O(n^2) & space: O(1)
        2. Sorting & 2 pointers
           - time: O(n log n) & space: O(1)
           - note: Python sort() uses Timsort, which has O(n) space
             complexity
        3. Hash set/map
           - time: O(n) & space: O(n)
           - set: have visited_set = set();
             if current num in the loop exists in the set -> dup
           - map (or dict): have a counter dict {num: occurence}
        4. bit manipulation - bitmasking
           - time: O(n) & space: O(1)
           - two separate bitmasks for non-negative and negative
           - >> shifting to mark visited numbers
           -- QUESTION: is >> operator O(1) time?
           - if any current num exists, return True

        [2,1,2,3]

         l 
           r
        [1,2,2,3]
        """
        return len(nums) > len(set(nums))
