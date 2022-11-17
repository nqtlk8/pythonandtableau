# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:15:52 2022

@author: admin
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_excel('articles.xlsx')

data.describe()
data.info()

data.groupby(['source_id'])['article_id'].count()
data.groupby(['source_id'])['engagement_reaction_count'].sum()
data = data.drop(['engagement_comment_plugin_count'], axis = 1)

def thisFuntion():
    print('This is my first funtion')
    
thisFuntion()

def aboutMe(name, surname, location):
    print('This is '+name + ' my surname is '+ surname + ' im from '+location)
    return name, surname , location
a= aboutMe('Quoc Thang', 'Nguyen','Dong Thap')

def favfood(food):
    for x in food:
        print('Top food is '+x)
fastfood = ['burgers','pizza','pie']
favfood(fastfood)

length = len(data)
keyword ='crash'
keyword_flag=[]

# for x in range (0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1 
#     else:
#         flag = 0
#     keyword_flag.append(flag)

def keywordflag(keyword):
    length = len(data)
    keyword_flag=[]
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1 
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
    
keywordflag = keywordflag('murder')

data['keyword_flag'] = pd.Series(keywordflag)


sent_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_neu_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

data.to_excel('blogme_clean.xlsx' , sheet_name = 'blogmedata' , index = False)

sources = pd.read_excel('1.3 BlogMe_sources.xlsx')

data1 = pd.read_excel('blogme_clean - Copy.xlsx')
data1 = pd.merge(data1, sources, on= 'Source Name' )

data1.to_excel('blogme_plus.xlsx', sheet_name = 'blogmedata', index = False)









