class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)
        if length%2 == 0:
            a = int(length/2)
            print ((nums3[a]+nums3[a-1])/2)
        else:
            a = int((length-1)/2)
            print (nums3[a])

nums1 = [1, 2]
nums2 = [3, 4]
c = Solution()
d = c.findMedianSortedArrays(nums1,nums2)