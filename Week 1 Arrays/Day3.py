# Remove Duplicates from Sorted Array
from numpy import diff


def removeDuplictates(nums):
     diff = 0
     for same in range(len(nums)):
        if nums[diff]!=nums[same]:
            diff+=1
            nums[diff],nums[same] = nums[same],nums[diff]
        
     
     return diff + 1

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplictates(nums)
print(nums,k)



# 1796. Second Largest Digit in a String
def secondHighest(self, s: str) -> int:
        largest = -1
        slargest = -1
        for letter in s:
            if 48<=ord(letter)<=57:
                num = int(letter)
                if num>largest:
                    slargest = largest
                    largest = num
                elif num>slargest and num!=largest:
                    slargest = num 
        return slargest

## Remove duplicates from sorted array

    
