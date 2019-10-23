from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}
        for i,num in enumerate(nums):
            if num not in lookup:
                lookup[target-num]=i
            else:
                return lookup[num],i
def t():
    a=[2, 7, 11, 15]
    b=9
    print(Solution().twoSum(a,b))
t()