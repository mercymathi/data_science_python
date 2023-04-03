#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
ama = pd.read_csv(r'C:\Users\Dell\Downloads\amazon data set\amazon.csv')
ama


# In[7]:


h = ama.head(10)
h


# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


cat = h['category']
cat


# In[23]:


per = [64,43,90,53,61,85,65,23,50,33]
per


# In[15]:


h[['category','discount_percentage']]


# In[16]:


plt.figure(figsize=(10,10))


# In[29]:


explode = (0,0,0.5,0,0,0,0,0,0,0)


# In[30]:


plt.pie(per,labels = cat,explode = explode,autopct='%1.1f%%',startangle = 70)
plt.axis('equal')
plt.title("amazon sales data set matplotlib exercise with first ten data")
plt.show()


# In[ ]:




