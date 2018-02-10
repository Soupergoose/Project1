# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:51:18 2018

Bitbot logic and function calls

@author: red5
"""
import os
import time
import poloniex
import bitbot

#Set working directory
os.chdir('******')

#Set Keys
###################################


#Set Shortcuts
polo = poloniex.Poloniex()


#fee is assumed to be 0.25%
fee = 0.0025
threshold = 0.01
#Considering profitability in regards to trades up to 'Days' old
Days = 7

#Currencies Dictionary *Type : Trade Eligible (T/F)*
Trade_eligibility = {'XRP' : False, 'STR' : False, 'NXT' : True, 'ETH' : False, 
'BTC': False, 'USDT' : False}
Current_Holdings = ('XRP', 'STR', 'NXT', 'ETH')
Base_Currencies = ('USDT', 'BTC')


Go = True
while Go == True:
    #Get Current Balances ***Matrix***
    balances = bitbot.Get_Balances(Current_Holdings, Base_Currencies)
    XRP_Balance = float(balances['XRP'])
    
    #Get Current Price Matrix
    price_matrix = bitbot.Get_Current_Price_Matrix(Base_Currencies, Current_Holdings)
    XRP_USDT = float(price_matrix[Current_Holdings.index('XRP'), Base_Currencies.index('USDT')])
    print(XRP_USDT)  
    
    #Analyze Open Orders
      
    #Recall previous purchase prices
    History = polo.returnTradeHistory('USDT_XRP', Days)
    XRP_lastbuy = 0.77
    XRP_lastsale = 0.86
    
    #Trade Eligible? Y/N
    if XRP_USDT_current > XRP_lastbuy * (1 + threshold):
            Potential_XRP_USDT_sell = True
            Potential_XRP_USDT_buy = False
            
    elif XRP_USDT_current < XRP_lastsale * (1 + threshold):
            Potential_XRP_USDT_sell = False
            Potential_XRP_USDT_buy = True
    else:   
            Potential_XRP_USDT_sell = False
            Potential_XRP_USDT_buy = False
            
    #Determine profitability
    if Potential_XRP_USDT_sell == True and XRP_Balance > 0:
        profit = (XRP_USDT*(1 + fee) - XRP_lastbuy)
        if profit > 0:
            SELL_XRP_USDT = True
            XRP_USDT_Sell_Amount = (profit/XRP_lastbuy)*XRP_Balance
            
    elif Potential_XRP_USDT_buy == True and USDT_Balance > 0:
        profit = (XRP_USDT*(1 + fee) - XRP_lastsale)
        if profit > 0: 
            BUY_XRP_USDT = True
            XRP_USDT_Buy_Amount = (profit/XRP_lastsale)*USDT_Balance
        
    
 ###########################################################       
def Average_Transaction(kind, currency_pair, Days):
    temp = polo.returnTradeHistory(currency_pair, Days)
    denominatorsum = 0
    numeratorsum = 0
    
    for i in range(len(temp)):
        Kind = temp[i]['type']
        
        if kind == Kind:
            denominatorsum += float(temp[i]['amount'])
            numeratorsum += float(temp[i]['amount']) * float(temp[i]['rate'])
            
    #Weighted average
    return numeratorsum/denominatorsum
   
  ################################################      
    
def Average_Price(history, currency, base):
    for i in range(len(history)):
        historical_price = history[i][currency]
        historical_quantity = history[i][
  #################################################          
        #Log all variables
        #Sleep
    time.sleep(180)
        #repeat
