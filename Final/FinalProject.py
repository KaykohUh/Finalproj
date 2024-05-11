#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[11]:


goog_stock = pd.read_csv(r'C:\Users\asmjehdfg\Desktop\DataSets\GOOG.csv')


# In[12]:


goog_stock.head


# In[32]:


goog_stock['50 Day MA'] = goog_stock['Close'].rolling(window=50).mean()
goog_stock['200 Day MA'] = goog_stock['Close'].rolling(window=200).mean()
goog_stock['52 Week High'] = goog_stock['Close'].rolling(window=52*5, min_periods=1).max()


# In[33]:


plt.figure(figsize=(10, 6))
plt.plot(goog_stock['Date'], goog_stock['Close'], label='Original Data')
plt.plot(goog_stock['Date'], goog_stock['50 Day MA'], label='50-Day Moving Average')
plt.plot(goog_stock['Date'], goog_stock['200 Day MA'], label='200-Day Moving Average')
plt.plot(goog_stock['Date'], goog_stock['52 Week High'], label='52-Week High')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('50-Day Moving Average')
plt.legend()


plt.show()


# In[21]:


goog_stock['Date'] = pd.to_datetime(goog_stock['Date'])
monthly_data = goog_stock.groupby(pd.Grouper(key='Date', freq='M')).mean()
plt.figure(figsize=(10, 6))
plt.plot(monthly_data.index, monthly_data['Close'], marker='o')
plt.xlabel('Date')
plt.ylabel('Mean Value')
plt.title('Google Average Stock (Monthly Close)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[28]:


sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Close", data=goog_stock)
plt.title('Google Stock Price (Close) Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[ ]:




