'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

# My Solution - 2 pointers in Sorted array
def fourSum(nums:list, target: int) -> list:
    nums.sort()
    sol = set()
    for a in range(len(nums)-1):
        for b in range(a+1,len(nums)):
            c,d = b+1,len(nums)-1
            while(c<d):
                sum = nums[a]+nums[b]+nums[c]+nums[d]
                if sum<target:
                    c+=1
                elif sum>target:
                    d-=1
                else:
                    sol.add(tuple([nums[a],nums[b],nums[c],nums[d]]))
                    c+=1
                    d-=1
                    while(c<d and nums[c]==nums[c-1]):c+=1
    return list(sol) 

# Best Approach - 2 pointers in Sorted array ( 3 optimizations)
def fourSum(nums: list, target: int) -> list:
        nums.sort()
        sol = []
        for a in range(len(nums)-1):
            if (a>0 and nums[a]==nums[a-1]):continue
            for b in range(a+1,len(nums)):
                if (b>a+1 and nums[b]==nums[b-1]):continue
                c,d = b+1,len(nums)-1
                while(c<d):
                    sum = nums[a]+nums[b]+nums[c]+nums[d]
                    if sum<target:
                        c+=1
                    elif sum>target:
                        d-=1
                    else:
                        sol.append([nums[a],nums[b],nums[c],nums[d]])
                        c+=1
                        d-=1
                        while(c<d and nums[c]==nums[c-1]):c+=1
        return sol 