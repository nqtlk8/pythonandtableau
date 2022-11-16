# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:10:24 2022

@author: admin
"""

import pandas as pd

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep =';')


CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemPurchased = 6

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = ProfitPerItem * NumberofItemPurchased
CostperTransaction = CostPerItem * NumberofItemPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberofItemPurchased

CostPerItem = data['CostPerItem']
NumberofItemPurchased = data['NumberOfItemsPurchased']
CostperTransaction = CostPerItem * NumberofItemPurchased

data['CostperTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostperTransaction']

data['Markup'] = data['ProfitPerTransaction'] / data['CostperTransaction']
data['Markup'] = round(data['Markup'], 2)


data.iloc[:,2]
data.iloc[:5]

day = data['Day'].astype(str)
year = data['Year'].astype(str)

my_date = day + '-' + data['Month'] + '-' + year
data['date'] = my_date

split_col = data['ClientKeywords'].str.split(',', expand = True)
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract']= split_col[2]

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

data['ItemDescription'] = data['ItemDescription'].str.lower()

seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

data = pd.merge(data , seasons , on = 'Month')

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop('Month', axis = 1)
data = data.drop('Year', axis = 1)


data.to_csv('ValueInc_Cleaned.csv', index = False)
