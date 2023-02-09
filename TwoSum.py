class Solution(object):
    def twoSum(self, nums, target):
        """:type nums: List[int]:type target: int:rtype: List[int]"""
        l=len(nums)
        a=[]
        for i in range(0,l):
            for j in range(i+1,l):
                m=nums[i]+nums[j]
                if m==target:
                    print(nums[i])
                    a.append(i)
                    a.append(j)
                    break
        return a
