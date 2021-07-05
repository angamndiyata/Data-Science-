#!/usr/bin/env python
# coding: utf-8

# In[53]:


#import pandas
import pandas as pd

#read the text file
df = pd.read_csv('balance.txt', delim_whitespace=True)

#find mean for each ethnicity
dr = (df.groupby(['Ethnicity']).mean())
print(dr[['Income']])

#find mean balance for married vs unmarried
dr1 = df.groupby(['Married']).mean()
print(dr1['Balance'])

#max income
print(df['Income'].max())

#find min income
print(df['Income'].min())

#number of cards
print(sum(df['Cards']))

#females vs males
print('Females :',(df.Gender == 'Female').count()) 
print('Males: ',(df.Gender == 'Male').count())


# In[ ]:




