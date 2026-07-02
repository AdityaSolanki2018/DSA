# Best time to buy and sell stocks - single transaction
def maxProfit(prices):
    minsofar = prices[0]
    profit = 0

    for i in range(0,len(prices)):
        minsofar = min(prices[i], minsofar)
        profit = max(profit,prices[i]-minsofar)

    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
    
                