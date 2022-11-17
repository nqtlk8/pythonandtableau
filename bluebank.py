# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:44:10 2022

@author: admin
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

json_file = open('loan_data_json.json')
data = json.load(json_file)
loandata = pd.DataFrame(data)

income = np.exp(loandata['log.annual.inc'])

a = 40
b= 500
if b > a:
    print('b is greater than a')

a = 40
b = 500
c = 1000
if b > a and b < c:
    print('b is greater than a but less than c')
    
c = 20
if b > a and b < c:
    print('b is greater than a and less than c')
else:
    print('no condition met')
    
a = 40
b = 500
c = 30

if b > a and b < c:
    print('b is greater than a and less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('no condition met')
    

lenght = len(loandata)
ficocat = []
for x in range(0,lenght):
    category = loandata['fico'][x]
    if category >= 300 and category < 400:
        cat = 'Very Poor'
    elif category >= 400 and category < 600:
        cat = 'Poor'
    elif category >= 601 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700:
        cat = 'Excellent'
    else:
        cat = 'Unknown'
    ficocat.append(cat)
        
    
ficocat = pd.Series(ficocat)
loandata['Fico.category'] = ficocat

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

catplot = loandata.groupby(loandata['Fico.category']).size()
catplot.plot.bar()
plt.show()

loandata['annualincome'] = income

loandata.to_csv('loancleaned.csv', index = True)





    
    
    
    
    
    
    
    
    
    
    