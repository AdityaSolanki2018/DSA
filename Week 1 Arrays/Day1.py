# Linear Search - Find Maximum element

# def max_element(arr:list)->int:
#     max = 0
#     for element in arr:
#         if element>max:
#             max = element
#     return max, arr.index(max)          # O(n) time complexity

# arr = [1]
# print(max_element(arr))

# Find minimum/maximum element in an array 
arr = [2,4,1,5,2,56,78,45,14]
minimum = float('inf')
for index,element in enumerate(arr):
    minimum = min(minimum,element)

print(minimum,arr.index(minimum))

# Leet code Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n):
            if i not in nums:
                return i
        return n
        