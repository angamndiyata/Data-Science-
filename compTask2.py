#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Import pandas
import pandas as pd

#Read data from the file called 'credit.csv' into a DataFrame called credit
#specify the delimiter is a single space
credit = pd.read_csv('credit.csv', delim_whitespace = 1)

#print the first 10 rows of the DataFrame
print(credit.sample(10))

#print Age and Education columns of the DataFrame
credit[['Age', 'Education']]

#select users above the age of 30
credit[credit.Age < 30 ]


# In[ ]:




