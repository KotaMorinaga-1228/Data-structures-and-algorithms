#!/usr/bin/env python
# coding: utf-8

# In[3]:


def euclid(m, n):
    # 課題１
    if (n>m):
        m,n = n,m
    while (n > 0):
        m,n=n,m%n
    return m

if __name__=='__main__':
    print(euclid(3,9))
    print(euclid(630,30))
    print(euclid(23566,2345))

