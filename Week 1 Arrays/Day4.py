# Problem: 1 Move zeroes to the end of the array

# Problem: 2 Sort Colours
def sortColors(nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[red],nums[i] =nums[i],nums[red]
                red+=1
        for i in range(n):
            if nums[i] == 1:
                nums[red],nums[i] =nums[i],nums[red]
                red+=1

#Problem: 3 Segregate Odd and Even numbers in an array
def segregateEvenOdd(arr):
    n = len(arr)
    even = 0
    for i in range(n):
        if i%2 == 0:
            arr[even], arr[i] = arr[i], arr[even]
            even+=1

arr = [0, 1, 2, 3, 4]
segregateEvenOdd(arr)
print(arr)
# Removing duplicates from sorted array (in-place)
# 2 pointer approach

# def removeDuplicates(nums) -> int:
#         if not nums:
#             return 0
#         slow = 0
#         for fast in range(1,len(nums)):
#             if nums[slow] != nums[fast]:
#                 slow+=1
#                 nums[slow] = nums[fast]
#         return slow + 1
            
# nums = [0,0,1,1,1,2,2,3,3,4]
# k = removeDuplicates(nums)
# print(k, nums)