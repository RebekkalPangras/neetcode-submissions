class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_list = set(nums)
        if len(unique_list) == len(nums):
            return False
        return True

        