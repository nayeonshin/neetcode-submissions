from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Questions
        1. What if not nums

        Let n be len(nums)

        Approaches
        1. Brute-force: 2 loops
        - O(n^2) time & O(1) space
        2. Hash map:
        - Keep a visited_nums_to_indices dict
        - One loop, look back if complement exists, return pair
        - O(n) time & O(n) space
        3. Sorting & 2 pointers
        - O(n log n) time & O(n) space
        [3,6,4,5] <- orig

        [(3, 0), (6, 1), (4, 2), (5, 3)]

                          r
            l
        [(3, 0), 4, 2), (5, 3), (6, 1)]
        """

        """
           v
        [3,4,5,6]

        visited_nums_to_indices = {
            3: 0,

        }
        """
        visited_nums_to_indices = defaultdict(int)

        for i, num in enumerate(nums):
            complement = target - num

            if complement in visited_nums_to_indices:
                return [visited_nums_to_indices[complement], i]
            
            visited_nums_to_indices[num] = i
        