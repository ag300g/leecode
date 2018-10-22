#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
给出一个股票的时序数据,返回最大获利的值

e.g. input: [10,9,8,7,2,5,6,11,3,9,4,15,5]
     ## (1) 只允许买卖一次: output: 12 (3块买进==15块卖出)
     ## (2) 允许任意次买卖, 卖出后才能再次买入: output: 26 (2买进--11卖出,3买进--9卖出,4买进--15卖出)
     ## (3) 最多允许N次买卖, 卖出后才能再次买入, 当N=2时: output: 21 (2买进--11卖出, 3买进--15卖出)

思路: 只需要记录当前价格最低点, 和当前的收益值就行
'''



class Solution:
    # @param prices, a list of integer
    # @return an integer

    ## (1)
    def maxProfit0(self, prices):
        if prices == []: return 0
        maxpro = 0
        buy = [prices[0]]
        lowest = prices[0]
        for i in prices[1:]:
            if i < lowest:
                lowest = i
            maxpro = max(maxpro, i - lowest)
        return maxpro

    ## (1)
    def maxProfit1(self, prices):
        max_profit = 0
        current_min_price = max(prices)
        for i in range(len(prices)):
            if prices[i] < current_min_price:
                current_min_price = prices[i]
            if prices[i]-current_min_price > max_profit:
                max_profit = prices[i]-current_min_price
        return max_profit

    ## (2)
    def maxProfit2(self, prices):
        if prices == []: return 0
        lowest = prices[0]
        maxpro = 0
        for i in range(len(prices)):
            if prices[i] > lowest:
               maxpro +=  prices[i]-lowest
            lowest = prices[i]
        return maxpro
    ## (3)
    def maxProfit3(self, prices):
        if prices == []: return 0
        maxtol, leftmax, rightmax = 0, 0, 0
        left = []
        low, high = prices[0], prices[-1]
        for i in range(len(prices)):
            leftmax = max(leftmax, prices[i] - low)
            left.append(leftmax)
            if prices[i] < low: low = prices[i]
        for j in range(len(prices) - 1, -1, -1):
            rightmax = max(rightmax, high - prices[j])
            maxtol = max(maxtol, left[j] + rightmax)
            if prices[j] > high: high = prices[j]
        return maxtol


if __name__ == '__main__':
    prices = [10, 9, 8, 7, 2, 5, 6, 11, 3, 9, 4, 15, 5]
    test = Solution()
    out0 = test.maxProfit0(prices)
    out1 = test.maxProfit1(prices)
    out2 = test.maxProfit2(prices)
    out3 = test.maxProfit3(prices)
    print(out0)
    print(out1)
    print(out2)
    print(out3)
