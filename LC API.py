#!/usr/bin/env python
# coding: utf-8

# In[20]:


#key
header = {'Authorization' : 'get your own key','Content-Type': 'application/json', 'Accept': 'application/json'}


# In[2]:


import requests


# In[43]:


summary = requests.get('https://api.lendingclub.com/api/investor/v1/accounts/#########/summary',headers=header)


# In[44]:


summary


# In[45]:


summary.json()

