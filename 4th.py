'''
Given the daily values of a stock, create a function called max_profit_days() that,
given a list of integers, will return the index value of the two elements that represent the day
on which one should have bought a share and the day on which one should have sold a share
based on the max profit. You are required to buy and sell only once.
You also must buy a stock before selling it.
You can assume that index 0 represents day 0 and index 7 represents day 7.
'''

def max_profit_days(stock_prices):

  trading_period = len(stock_prices)
  max_profit = None
  buy_day = None
  sell_day = None

  for buy in range(trading_period - 1):
    for sell in range(buy + 1, trading_period):
      profit = stock_prices[sell] - stock_prices[buy]
      if max_profit == None or max_profit < profit:
        max_profit = profit
        buy_day = buy
        sell_day = sell

  return (buy_day, sell_day)




print(max_profit_days([17, 11, 60, 25, 150, 75, 31, 120]))