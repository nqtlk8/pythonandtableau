# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:07:30 2022

@author: admin
"""

import pandas as pd

#Import data
data_BHX_01 = pd.read_excel('Gia_BHX_2022-12-01.xlsx')
data_BHX_15 = pd.read_excel('Gia_BHX_2022-12-15.xlsx')
data_Winmart_01 = pd.read_excel('Gia_Winmart_2022-12-01.xlsx')
data_Winmart_15 = pd.read_excel('Gia_Winmart_2022-12-15.xlsx')

#Kiem tra gia tri Null
data_BHX_01.isnull().sum()
data_BHX_15.isnull().sum()
data_Winmart_01.isnull().sum()
data_Winmart_15.isnull().sum()
# gop du lieu
data_BHX = data_BHX_01.merge(data_BHX_15)
data_Winmart = data_Winmart_01.merge(data_Winmart_15, on ='Tên sản phẩm', how = 'inner')
data_BHX.info()



#xoa cac cot du thua
data_BHX = data_BHX.drop(data_BHX[['Sku_y','Tên sản phẩm_y','LinkCategory_y','LinkSku_y']], axis = 1)
data_Winmart.info()
data_Winmart = data_Winmart.drop(data_Winmart[['Category_link_y','Tên sản phẩm_y']], axis = 1)

data_Winmart_dul = data_Winmart.duplicated()
data_Winmart_dul.value_counts()
data_BHX_dul = data_BHX.duplicated()
data_BHX_dul.value_counts()

data_Winmart.isnull().sum()

data_BHX['Barcode'].duplicated().value_counts()
data_Winmart['Tên sản phẩm_x'].duplicated().value_counts()



