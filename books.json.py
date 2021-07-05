#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import json

import json


# In[8]:


#initiate a dict called data
#add a list of books into data
#using append add book information about title,authour,year and publisher saved into a dict.

data = {}
data['book'] = []
data['book'].append({'title' : ' Becoming ' ,
                    'author' : 'Michelle Obama' ,
                    'year' : '2018',
                    'Publisher' : 'Crown Publishing',
                     })
data['book'].append({'title' : ' THE ART OF STATISTICS ' ,
                    'author' : 'David Spiegelhalter' ,
                    'year' : '2019',
                    'Publisher' : 'Basic Books',
                     })
data['book'].append({'title' : ' Infinite Powers: How Calculus Reveals the secret of the Universe' ,
                    'author' : 'Steven Strogatz' ,
                    'year' : '2020',
                    'Publisher' : 'Mariner Books',
                     })
data['book'].append({'title' : 'The Joy of x: A guided tour of Math,from One to Infinity ' ,
                    'author' : 'Stevens Strigatz' ,
                    'year' : '2017',
                    'Publisher' : 'Mariner Books',
                     })
data['book'].append({'title' : 'Zeros: The Biography of dangerous Idea' ,
                    'author' : 'Charles Seife' ,
                    'year' : '1997',
                    'Publisher' : 'Viking Adult',
                     })
data['book'].append({'title' : 'Proofness: How You are Being Fooled by Numbers' ,
                    'author' : 'Charles Seife' ,
                    'year' : '2010',
                    'Publisher' : 'Viking Adult',
                     })
data['book'].append({'title' : ' Decoding the Universe' ,
                    'author' : 'Charles Seife' ,
                    'year' : '2007',
                    'Publisher' : 'Viking Adult',
                     })

#once all 6 books are added, write them into a text file called books.txt. 

with open('books.txt','w') as outfile:
    json.dump(data, outfile)


# In[ ]:




