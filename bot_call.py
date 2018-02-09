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
    #Get Current Balances
    balances = bitbot.Get_Balances(Current_Holdings, Base_Currencies)
    XRP_Balance = float(balances['XRP'])
    
    #Get Current Prices
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
    if Potential_XRP_USDT_sell == True:
        profit = (XRP_USDT*(1 + fee) - XRP_lastbuy)
        if profit > 0:
            SELL_XRP_USDT = True
            XRP_USDT_Sell_Amount = (profit/XRP_lastbuy)*XRP_Balance
            
        
    
        #log all variables
        
        #Sleep
    time.sleep(180)
        #repeat
