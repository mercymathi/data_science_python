#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
cd = pd.read_csv('C:\\Users\\Dell\\Downloads\\carsales\\car_sales.csv')#encoding=('ISO-8859-1'))
cd


# In[101]:


#h=cd.head(10)
#h
#f = h.fillna(00.00)
#f
cd[['Manufacturer','Sales_in_thousands','Price_in_thousands']].head(10)


# In[73]:


cd.size


# In[74]:


h.size


# In[75]:


cd.shape


# In[76]:


h.shape


# In[77]:


h.columns


# In[80]:


x_feature = f[['__year_resale_value','Price_in_thousands']]
x_feature.head(10)


# In[81]:


y_target = f[['Sales_in_thousands']]
y_target.head(10)


# In[82]:


x_feature.shape


# In[83]:


y_target.shape


# In[84]:


#split test and training data 75% and 25% testing data

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x_feature,y_target)


# In[85]:


print(x_train.shape)


# In[86]:


print(y_train.shape)


# In[87]:


print(x_test.shape)


# In[88]:


print(x_test.shape)


# In[89]:


#linear regression model

from sklearn.linear_model import LinearRegression
lg = LinearRegression()
lg.fit(x_train,y_train)


# In[93]:


pre = lg.predict(x_test)
pre


# In[95]:


#import required libraries for calculating MSE(mean sqaure error)

from sklearn import metrics
import numpy as np


print (np.sqrt(metrics.mean_squared_error (y_test,pre)))


# In[ ]:





# In[ ]:





# In[ ]:




