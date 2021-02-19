#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gcdd(a,b):
    if b==0:
        return a
    else:
        return gcdd(b,a%b)

lst=[357,234]
print(gcdd(lst[0],lst[1]))


# In[ ]:





# In[ ]:




