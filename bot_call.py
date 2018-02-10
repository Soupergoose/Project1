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
    
    
    #Cancel Open Orders If Necessary.
    polo.cancelOrder('ordernumber')
      
    #Recall previous purchase prices
    History = polo.returnTradeHistory('USDT_XRP', Days)
    (XRP_last_buy, XRP_lastsale) = Last_Prices(History)
 ##############################
    def Last_Prices(History):
        buy = 0
        sale = 0
        counter = 0
        while buy == 0 or sell == 0:
            temp = History[counter]['type']
            if temp == 'buy' and buy == 0:
                XRP_lastbuy = float(History[counter]['rate'])
                buy = 1
            elif temp == 'sell' and sale == 0:
                XRP_lastsale = float(History[counter]['rate'])
                sale = 1
            else: counter += 1
        return XRP_lastbuy, XRP_lastsale
 #########################################   
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
# Average_Transaction calculates both average and weighted average of previous purchases/sales.
def Average_Transaction(kind, currency_pair, Days, Weighted):
    temp = polo.returnTradeHistory(currency_pair, Days)
    denominatorsum = 0
    numeratorsum = 0
    
    for i in range(len(temp)):
        Kind = temp[i]['type']
        
        if kind == Kind:
            Temp = float(temp[i]['amount'])
            denominatorsum += Temp
        if Weighted == 1:
            numeratorsum += Temp * float(temp[i]['rate'])
        if Weighted == 0: 
            numeratorsum += Temp
    #Weighted average
    return numeratorsum/denominatorsum
   

  #################################################          
        #Log all variables
         
        #Make Trades
        if BUY_XRP_USDT == True:
            #Returns order number and info that should be logged.
            log(polo.buy('currency_pair', 'rate', 'amount'))
            
        elif SELL_XRP_USDT == True:
            log(polo.sell('currency_pair', 'rate', 'amount'))
        
        else: log('No Trade')
  
        #Sleep
    time.sleep(180)
        #repeat
