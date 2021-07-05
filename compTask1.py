#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[13]:


#Why doesn’t 
#np.array((1, 0, 0), (0, 1, 0), (0, 0, 1,dtype=float) 
#create a two dimensional array? Write it the correct way.

#Answer : The list for each row array is missing, matrix [] brackets mising for matrix array and the datatype uses wrong syntax.
         

#correct way to represent the array.
np.array([[(1, 0, 0)], [(0, 1, 0)], [(0, 0, 1)]], dtype=float)


# In[10]:


#What is the difference between 
a = np.array([0, 0, 0]) 
print(a) 
#and 
a =np.array([[0, 0, 0]]) 
print(a)
#?

#Answer  : 1. array of single item where a[0] = 0 and 2. array of a row array where a[0] = [0,0,0]


# In[110]:


# A 3 by 4 by 4 is created with 
arr = np.linspace(1, 48,48).reshape(3, 4, 4) 
print("Array")
print(arr)
#Index or slice this array to obtain the following

print("1st")
print(arr[1][0,3])

print("2nd")
print(arr[0][2])

print("3rd")
print(arr[2])

print("4rd")
print(np.array([arr[0][1,[0,1]],arr[1][1,[0,1]],arr[2][1,[0,1]]]))

print("5th")
print(np.array([arr[2][0,[2,3]][::-1],arr[2][1,[2,3]][::-1],arr[2][2,[2,3]][::-1],arr[2][3,[2,3]][::-1]]))

print("6th")
print(np.array([arr[0][:,0][::-1], arr[1][:,0][::-1] , arr[2][:,0][::-1]]))

print("7th")
print(np.array([[arr[0][0,0],arr[0][0,3]],[arr[2][3,0],arr[2][3,3]]]))

print("8th")
print(np.array([arr[1][2,:],arr[1][3,:],arr[2][0,:],arr[2][1,:]]))


# In[ ]:


■ 20.0
■ [ 9. 10. 11. 12.]
■ [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
■ [[5. 6.], [21. 22.] [37. 38.]]
■ [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
■ [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
■ [[1. 4.] [45. 48.]]
■ [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
Hint: use flatten (help here) and reshape.


# In[97]:


print("5th")
print([arr[2][0,[2,3]][::-1],[arr[2][1,[2,3]][::-1],[arr[2][2,[2,3]][::-1],[arr[2][3,[2,3]][::-1]]


# In[ ]:




