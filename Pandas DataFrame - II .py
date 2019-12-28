#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


from numpy.random import randn


# In[3]:


np.random.seed(101)


# In[4]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[5]:


df


# #### Conditional Selection

# In[6]:


df > 0


# In[8]:


booldf = df[df>0]


# In[9]:


booldf


# In[11]:


#conditions on individual columns or series
df['X']>0


# In[12]:


df['X']


# In[14]:


#It will return only true values of W or the values of W that is greater than 0.
df[df['W']>0]


# In[15]:


df[df['Z']<0]


# In[16]:


#creating subset of the original dataframe by removing unwanted columns or useless columns through conditional selection
subdf = df[df['W']>0]


# In[17]:


subdf


# In[19]:


#now taking the column X only out of the subdf not the original df
subdf['X']


# In[20]:


#since this is dataframe we can perform both of the above steps combined
df[df['W']>0]['X']


# In[21]:


#or even multiple columns like:
df[df['W']>0][['X','Y']]


# In[30]:


#breaking above unified step into individual steps like:
boolser = df['W']>0
result = df[boolser]
my_cols = ['Y','X']


# In[31]:


result[my_cols]


# In[36]:


#using multiple condtions in a single line of code(python's normal 'and operator cannot be used here as pythos's and operator
# works on a single boolean value and df['W'] here will have a series of boolean values as well as in df['X'])
df[(df['W']>0) & (df['X']<0)]


# In[37]:


#same goes for 'or' operator | is used instead
df[ (df['W']>0) | (df['X']>1)]


# In[38]:


df


# In[39]:


#resetting index back to default in a dataframe
df.reset_index()# it wil cause to change the existing index to a column named index and a new numeric index will be created


# In[41]:


#By default inplace is set to false therefore:
#resetting index as above won't make any permanent changes to the origina dataframe as inplace has not been defined so:
df.reset_index(inplace=True)


# In[42]:


df


# In[44]:


ind = 'UP UK DL TN KL'.split()


# In[45]:


ind


# In[46]:


df['States'] = ind


# In[47]:


df


# In[50]:


#incase we want to add a existing column as the new index we use set_index instead of reset_index as:
df.set_index('States')#Permanent changes won't occur as inplace value is set to false as default


# In[51]:


df.set_index('States', inplace=True)


# In[52]:


df


# In[53]:


df.reset_index()


# In[54]:


df.set_index('index', inplace=True)


# In[55]:


df


# In[ ]:




