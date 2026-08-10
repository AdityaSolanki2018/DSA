# Remove Duplicates from Sorted Array
from ast import List

from numpy import diff

def removeDuplicates(nums: list) -> int:
        slow, fast = 0,0
        for i in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1 
        return slow + 1

# def removeDuplictates(nums):
#      diff = 0
#      for same in range(len(nums)):
#         if nums[diff]!=nums[same]:
#             diff+=1
#             nums[diff],nums[same] = nums[same],nums[diff]
        
     
#      return diff + 1

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(nums,k)

# # Remove Elemet 27
# def removeElement(self, nums: List[int], val: int) -> int:
#         n = len(nums)
#         slow = 0
#         for fast in range(n):
#             if nums[fast] != val:
#                 nums[slow],nums[fast] = nums[fast],nums[slow]
#                 slow+=1
#         return slow

# # Remove Duplicates from Sorted Array II


# # 1796. Second Largest Digit in a String
# def secondHighest(self, s: str) -> int:
#         largest = -1
#         slargest = -1
#         for letter in s:
#             if 48<=ord(letter)<=57:
#                 num = int(letter)
#                 if num>largest:
#                     slargest = largest
#                     largest = num
#                 elif num>slargest and num!=largest:
#                     slargest = num 
#         return slargest

## Remove duplicates from sorted array

    
