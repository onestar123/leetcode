class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for k, i in enumerate(nums):
            dict1[i] = k
            if target - i in dict1 and i is not target - i:
                return [dict1[target - i], dict1[i]]
        nums = [4, 3, 5, 15]
        target = 8
        s = Solution()
        print(s.twoSum(nums, target))