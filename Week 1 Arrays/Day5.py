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


# Best Time to Buy and Sell Stock
def maxProfit(prices: list) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit