class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Questions
        1. What if len(nums) == 1 or 0?

        Let n be len(nums)

        Approaches
        1. Brute-force: using 2 loops - O(n^2) time & O(1) space
        2. Sorting & 2 pointers: O(n log n) time & O(n) space
        - nums.sort() -> O(n) space
        - sorted(nums) -> O(n) space
        3. Hash set/map (or dict) - O(n) time & O(n) space
        - set: keep visited_nums set, if exists return True
        - dict: num -> # occurences, if any occurence > 1 True
        4. Bitmask as hash set - same complexity as 1
        - use bitmask as alternative to visited_nums set
          -- O(1) space
        - 2 bitmasts for non-negative and negative nums
          respectively
        - << >> operator - not O(1) time
        """
        return len(nums) > len(set(nums))

        #        v
        # [1,2,3,3]

        # # (1,2,3)
        # visited_nums = set()

        # for num in nums:
        #     if num in visited_nums:
        #         return True
            
        #     visited_nums.add(num)
        
        # return False