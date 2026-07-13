# Second Largest number in an array
from random import random


def second_largest(arr:list)->int:
    largest = 0
    secondlargest = 0
    for i in range(len(arr)):
        if arr[i]> largest:
            secondlargest = largest
            largest = arr[i]
        elif arr[i]> secondlargest and arr[i]!=largest:
            secondlargest = arr[i]
    return secondlargest

arr = [1, 2, 3, 4, 5]
print(second_largest(arr))

# Kth largest number in an array
class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
