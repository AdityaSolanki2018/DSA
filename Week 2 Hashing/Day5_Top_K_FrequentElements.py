'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

from collections import defaultdict

# using heapq
import heapq
# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     d = defaultdict(int)
#     for num in nums:
#         d[num]+=1
#     heap = []
#     for key,val in d.items():
#         if len(heap) < k or val > heap[0][0]:
#             heapq.heappush(heap,[val,key])
#         if len(heap) > k:
#             heapq.heappop(heap)
#     return [i[1] for i in heap]

# Using Bucket Sort
from collections import Counter

def topKFrequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in counts.items():
        buckets[freq].append(num)
        
    ans = []
    for freq in range(len(nums), 0, -1):
        for num in buckets[freq]:
            ans.append(num)
            if len(ans) == k:
                return ans
    return ans


# def topKFrequent(nums: list[int], k: int) -> list[int]:
#         d = defaultdict(int)
#         for num in nums:
#             d[num]+=1
#         heap = []

#         arr = [[0]]*(len(nums)+1)
#         print(arr)
#         for key,val in d.items():
#             print(val)
#             if arr[val] != [0]:
#                 arr[val].append(key)
#             else:arr[val] = [key]
    
#         print(arr)
#         ans = []
#         i = len(arr)-1
#         while(i>=0 & len(ans)<k):
#             if arr[i] != [0]:
#                 ans.append(arr[i])
#             i-=1
#         return ans

print(topKFrequent([1], 1))