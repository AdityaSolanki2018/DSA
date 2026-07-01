# Move Zeros to the end of the array
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    zeroindex = 0
    for i in range(n):
        if nums[i] != 0:
            nums[zeroindex],nums[i] = nums[i],nums[zeroindex]
            zeroindex+=1