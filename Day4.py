# Removing duplicates from sorted array (in-place)
# 2 pointer approach

def removeDuplicates(nums) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1,len(nums)):
            if nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
        return slow + 1
            
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k, nums)