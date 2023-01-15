# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:07:30 2022

@author: admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Import data
data_BHX_01 = pd.read_excel('Gia_BHX_2022-12-01.xlsx')
data_BHX_15 = pd.read_excel('Gia_BHX_2022-12-15.xlsx')
data_Winmart_01 = pd.read_excel('Gia_Winmart_2022-12-01.xlsx')
data_Winmart_15 = pd.read_excel('Gia_Winmart_2022-12-15.xlsx')

# Gop du lieu ngay 01 va ngay 15 lai voi nhau
data_BHX = data_BHX_01.merge(data_BHX_15,on = 'Sku', how = 'outer')
data_Winmart = data_Winmart_01.merge(data_Winmart_15, on ='Tên sản phẩm', how = 'outer')
data_BHX.info()
data_Winmart.info()

#Xoa columns khong can thiet
data_BHX = data_BHX.drop(data_BHX[['Tên sản phẩm_y','Barcode_y','LinkCategory_y','LinkSku_y']], axis = 1)
data_Winmart = data_Winmart.drop(data_Winmart[['Category_link_y','Url_y','Sell unit_y']], axis = 1)

#Kiem tra gia tri null
data_BHX.isnull().sum()
data_BHX = data_BHX.dropna()
data_Winmart.isnull().sum()
data_Winmart = data_Winmart.dropna()
#Kiem tra Duplicate
data_BHX.duplicated().sum()
data_BHX = data_BHX.drop_duplicates()
data_Winmart.duplicated().sum()

#Tao column Category
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.split(".com/")[-1])
data_Winmart['Category_link_x'] = data_Winmart['Category_link_x'].apply(lambda x: x.split(".vn/")[-1])

#Nhom cac san pham cung cong nang
data_BHX['LinkCategory_x'].value_counts()

data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('ca-phe-tra','Ca_Phe_Tra'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('ca-phe-hoa-tan','Ca_Phe_Tra'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('ca-phe-phin','Ca_Phe_Tra'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('ca-phe-lon','Ca_Phe_Tra'))

data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('mi','Mi_Pho'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('mi-nui-bun-kho','Mi_Pho'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('mi-pho-chao-an-lien','Mi_Pho'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('Mi_Pho-nui-bun-kho','Mi_Pho'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('Mi_Pho-pho-chao-an-lien','Mi_Pho'))

data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('nuoc-giat','Nuoc_Giat'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('nuoc-giat-cho-tre','Nuoc_Giat'))
data_BHX['LinkCategory_x'] = data_BHX['LinkCategory_x'].apply(lambda x: x.replace('Nuoc_Giat-cho-tre','Nuoc_Giat'))

data_Winmart['Category_link_x'].value_counts()

data_Winmart['Category_link_x'] = data_Winmart['Category_link_x'].apply(lambda x: x.replace('mi-thuc-pham-an-lien--c34','Mi_Pho'))
data_Winmart['Category_link_x'] = data_Winmart['Category_link_x'].apply(lambda x: x.replace('mi--c01145','Mi_Pho'))
data_Winmart['Category_link_x'] = data_Winmart['Category_link_x'].apply(lambda x: x.replace('mien-hu-tiu-banh-canh--c01148','Mi_Pho'))
data_Winmart['Category_link_x'] = data_Winmart['Category_link_x'].apply(lambda x: x.replace('pho-bun--c01147','Mi_Pho'))

data_Winmart['Category_link_x'] = data_Winmart['Category_link_x'].apply(lambda x: x.replace('ca-phe--c01162','Ca_Phe_Tra'))

data_Winmart['Category_link_x'] = data_Winmart['Category_link_x'].apply(lambda x: x.replace('nuoc-giat--c01140','Nuoc_Giat'))

#Del, rename columns
data_BHX = data_BHX.drop(data_BHX[['Sku','Barcode_x','LinkSku_x','DateUpdate_x','DateUpdate_y']], axis = 1)
data_BHX.columns = ['Ten_San_Pham','Gia_01','Danh_Muc','Gia_15']

data_Winmart = data_Winmart.drop(data_Winmart[['Url_x','Sell unit_x']], axis = 1)
data_Winmart.columns = ['Danh_Muc','Ten_San_Pham','Gia_01','Gia_15']

#Kiem tra lai gia tri Null va Duplicate
data_BHX.isnull().sum()
data_Winmart.isnull().sum()

data_BHX.duplicated().sum()
data_BHX = data_BHX.drop_duplicates()

data_Winmart.duplicated().sum()
data_Winmart = data_Winmart.drop_duplicates()

#Chuyen doi column Gia_01 va Gia_15 sang Int

data_BHX['Gia_01'] = data_BHX['Gia_01'].str.replace('₫', '')
data_BHX['Gia_01'] = data_BHX['Gia_01'].str.replace('.', '').astype(int)

data_BHX['Gia_15'] = data_BHX['Gia_15'].str.replace('₫', '')
data_BHX['Gia_15'] = data_BHX['Gia_15'].str.replace('.', '').astype(int)

data_Winmart['Gia_01'] = data_Winmart['Gia_01'].str.replace('₫', '')
data_Winmart['Gia_01'] = data_Winmart['Gia_01'].str.replace('.', '').astype(int)

data_Winmart['Gia_15'] = data_Winmart['Gia_15'].str.replace('₫', '')
data_Winmart['Gia_15'] = data_Winmart['Gia_15'].str.replace('.', '').astype(int)

# Tao column Chenh Lech Gia

data_BHX['Chenh_Lech_Gia'] = data_BHX['Gia_15'] - data_BHX['Gia_01']
data_Winmart['Chenh_Lech_Gia'] = data_Winmart['Gia_15'] - data_Winmart['Gia_01']

#Tao bang so sanh hang hoa cua BHX va Winmart

data_BHX['Danh_Muc'].value_counts()
data_Winmart['Danh_Muc'].value_counts()

Danh_Muc = data_BHX['Danh_Muc'].value_counts().keys().tolist()
Danh_Muc

So_Luong_SP_BHX = [378, 312,284 , 178, 1]
So_Luong_SP_Winmart = [0, 6, 200, 92, 0]

barWidth = 0.25
fig = plt.subplots(figsize =(7, 5))

br1 = np.arange(len(So_Luong_SP_BHX))
br2 = [x + barWidth for x in br1]
 
plt.bar(br1, So_Luong_SP_BHX, color ='r', width = barWidth,
         label ='BHX')
plt.bar(br2, So_Luong_SP_Winmart, color ='g', width = barWidth,
         label ='Winmart')

plt.xlabel('Danh Muc', fontweight ='bold', fontsize = 15)
plt.ylabel('So Luong', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(So_Luong_SP_BHX))],
        Danh_Muc)
 
plt.legend()
plt.show()

#Tao bang chenh lech gia

fig, ax = plt.subplots()
ax.scatter(data_BHX['Danh_Muc'], data_BHX['Chenh_Lech_Gia'])

fig, ax = plt.subplots()
ax.scatter(data_Winmart['Danh_Muc'], data_Winmart['Chenh_Lech_Gia'])

#Dem so luong san pham tang/giam gia theo danh muc
data_BHX.count()
data_Winmart.count()
data_Winmart['Danh_Muc'].value_counts()
data_BHX['Danh_Muc'].value_counts()

data_BHX['Chenh_Lech_Gia'][(data_BHX['Chenh_Lech_Gia'] < 0) & (data_BHX['Danh_Muc'] == 'Ca_Phe_Tra')].count()