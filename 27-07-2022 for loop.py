#!/usr/bin/env python
# coding: utf-8

# In[4]:


x="abcd"
"d" in x


# In[6]:


"d" not in x


# In[7]:


x=[1,2,3,"ab"]


# In[8]:


"ab" in x


# In[9]:


#sequential data type ------- string, list, sets, tuple, dictionary


# In[10]:


x="abc"
for y in x:
    print(y)


# In[11]:


x="abcdefghijklmnopqrstuvwxyz"
for y in x:
    print(y)


# In[12]:


x="abcdefghijklmnopqrstuvwxyz"
for y in x:
    print(y)
    print("hi")


# In[13]:


x=[1,2,3,"a"]
for y in x:
    print(y)


# In[14]:


x=(1,2,3,"a")
for y in x:
    print(y)


# In[17]:


x={"name":"kushal","age":22,"height":167.5,"weight":61}

for y in x:
    print(y)


# In[20]:


x={"name":"kushal","age":22,"height":167.5,"weight":61}

for y in x.values():
    print(y)


# In[22]:


x={"name":"kushal","age":22,"height":167.5,"weight":61}

for z,y in x.items():
    print(z,y)


# In[23]:


#range(starting range, ending range)#--------sequential data type


# In[25]:


range(1,100)
for y in range(1,100):
    print(y)


# In[26]:


range(1,100)
for y in range(1,10):
    print(y)


# # step size

# In[29]:


range(1,100)
for y in range(0,10,2):
    print(y)


# In[30]:


range(1,100)
for y in range(0,10,3):
    print(y)


# In[33]:


range(1,100)
for y in range(0,10):
    if y==5:
         print(y)


# In[7]:


range(1,100)
for y in range(1,10):
    if y==5:
        break
    print(y)


# In[ ]:


#reverse order


# In[1]:


range(1,100)
for y in range(10,0,-1):
    print(y)


# In[2]:


range(1,100)
for y in range(100,10,-1):
    print(y)


# In[5]:


range(1,100)
for y in range(1,10):
    if y==5:
        break
    print(y)


# In[6]:


range(1,100)
for y in range(1,10):
    if y==5:
        continue
    print(y)


# In[10]:


range(1,100)
for y in range(1,10):
    if y==5:
        continue
    print(y,end=" ")


# In[ ]:




