from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        idx,f=divmod(len(nums1)+len(nums2),2)
        p1,p2=0,0
        l=-1
        s=0
        while l<idx-1:
            if  p1 ==len(nums1):
                s=nums2[p2]
                p2+=1
            elif p2==len(nums2):
                s=nums1[p1]
                p1+=1
            elif nums1[p1]>nums2[p2]:
                s=nums2[p2]
                p2+=1
            else:
                s=nums1[p1]
                p1+=1
            l+=1
        if p1 == len(nums1):
            r=nums2[p2]

        elif p2 == len(nums2):
            r=nums1[p1]

        elif nums1[p1]>nums2[p2]:
            r=nums2[p2]
        else:
            r=nums1[p1]
        if f:
            return r
        else:
            return (s+r)/2
print(Solution().findMedianSortedArrays([1,2],[]))
