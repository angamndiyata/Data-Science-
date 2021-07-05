#!/usr/bin/env python
# coding: utf-8

# In[18]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
car_data = pd.read_csv('Cars93.csv')

# Inline indicates to present graphs as cell output
# read_csv returns a DataFrame, the file path is relative to that of your notebook.


# In[19]:


print(car_data.columns)
car_data.head(2)


# #### We are able to see how many Manufacturers we have in the data by using the unique() function below:

# In[20]:


car_data['Manufacturer'].unique()


# ##### Using Group-by’s and Merges
# Group-by’s can be used to build groups of rows based on a specific feature in your dataset eg. the ‘Manufacturer’ categorical column. 

# In[21]:


group_by_Manufacturer = car_data.groupby(by=['Manufacturer'])

car_data_avg = round(group_by_Manufacturer.mean(),0)
car_data_avg


# ##### With the generated dataset above we are able to do better visualizations for the data set 

# In[22]:


# Since all the columns in car_data_count are the same, we will use just the first column as the rest yield the same result. iloc allows us to take all the rows and the zeroth column.

car_data_count_series = car_data_avg.iloc[5:5,1]


## we will assemble a DataFrame of only the relevant features to plot  
features_of_interest = pd.DataFrame({'EngineSize': car_data_avg['EngineSize'],
                                     'Passengers': car_data_avg['Passengers'],
                                   }
                                   )

## Let us plot a few of the manufactures for visibility
features_of_interest = features_of_interest.iloc[:10,]
features_of_interest.plot(kind='bar')


# #### Stacked bar graph

# In[23]:


features_of_interest.plot.bar(stacked=True)


# In[32]:


#### Hosrizontal bar graph


# In[24]:


features_of_interest.plot.barh(stacked=True)


# #### Want to try pie charts? Lets do it

# ##### Lets prepare some data. We can create a pie chart to show the population of categorical variables 

# In[25]:


# group by passengers 
group_by_Passengers = car_data.groupby(by=['Type'])

car_typePassengers = group_by_Passengers.count()

# get first column
car_typePassengers = pd.DataFrame(car_typecount.iloc[:,0])

car_typePassengers.rename(columns={'Manufacturer': 'Passengers'}, inplace=True)

car_typePassengers.plot.pie(subplots=True,figsize=(8, 8))


# In[68]:





# group by Type 
group_by_Type = car_data.groupby(by=['Type'])

car_typecount = group_by_Type.count()

car_typecount = pd.DataFrame(car_typecount.iloc[:,0])

car_typecount.rename(columns={'Manufacturer': 'Type'}, inplace=True)

car_typecount.plot.pie(subplots=True,figsize=(8, 8))


# In[26]:


# Group by Airbags
group_by_AirBags = car_data.groupby(by=['AirBags'])

car_AirBagscount = group_by_AirBags.count()

car_AirBagscount = pd.DataFrame(car_AirBagscount.iloc[:,0])

car_AirBagscount.rename(columns={'Manufacturer': 'Airbags'}, inplace=True)


car_AirBagscount.plot.pie(subplots=True,figsize=(8, 8))


# ## 7 other types of visualisation

# 1. We do a correlogram to look at the correlation of all variables.

# In[83]:


import seaborn as sns
# Plot
plt.figure(figsize=(12,10), dpi= 80)
sns.heatmap(car_data.corr(), xticklabels=car_data.corr().columns, yticklabels=car_data.corr().columns, cmap='RdYlGn', center=0, annot=True)

# putting keys to make data easier to read and understand.
plt.title('Correlogram of cars', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()


# ## 2. We compare similarities according to Model.

# In[36]:


import scipy.cluster.hierarchy as shc
df = car_data
plt.figure(figsize=(16, 10), dpi= 80)  
plt.title("Model Dendograms", fontsize=22)  
dend = shc.dendrogram(shc.linkage(df[['Price', 'EngineSize', 'Weight']], method='ward'),labels=df.Model.values, color_threshold=100)  
plt.xticks(fontsize=12)
plt.show()


# ## 3. Violin Plot of MPG.highway for the Manufacturers

# In[56]:


plt.figure(figsize=(13,10), dpi= 80)
sns.violinplot(x='Manufacturer', y='MPG.highway', data=df, scale='width', inner='quartile')

# Decoration
plt.title('Violin Plot of Highway by Vehicle Manufacturers', fontsize=7)
plt.show()


# ## 4. We explore all possible numerical relationships.

# In[59]:


# Plot
plt.figure(figsize=(10,8), dpi= 80)
sns.pairplot(df, kind="reg", hue="species")
plt.show()


# Preparation of data to get only numeric data.

# In[74]:


df = car_data
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df1 = df.select_dtypes(include=numerics)
df1.head(5)


# ## 5. Linear Regression of Price and Engine size

# In[80]:


sns.regplot(x="Price", y="EngineSize", data=df1)


# ## 6. Linear regression separated according to origin.

# In[82]:


sns.lmplot(x="Weight", y="Price", hue="Origin", data=car_data)


# ## 7. Plot distribution according to Origin in a pie chart

# In[89]:


df2 = car_data.groupby(by=['Origin'])
df2.head()


# In[90]:


car_typecount = df2.count()

car_typecount = pd.DataFrame(car_typecount.iloc[:,0])

car_typecount.rename(columns={'Manufacturer': 'Make'}, inplace=True)

car_typecount.plot.pie(subplots=True,figsize=(8, 8))


# In[ ]:




