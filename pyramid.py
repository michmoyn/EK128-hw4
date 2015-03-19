
# coding: utf-8

# In[3]:

import string
def pyramid(n):
    letters= (string.ascii_lowercase)*n
    a= 0
    b= 2
    c= ""
    for x in range (0,n):
        for i in range (0,x+1):
            c += letters[a]
            a += 1
        for i in range (0,x):
            c += letters[a-b]
            b += 1
        b = 2
        print (c.center(2*n -1, "-"))
        c = ""


# In[5]:

import string
def pyramid2(n):
    letters = (string.ascii_lowercase)*n
    a = 0 
    b = 2
    c = ""
    d = ""
    for x in range(0,n):
        for i in range(0,x+1):
            c += letters[a]
            a += 1
        for i in range(0,x):
            c +=letter[a-b]
            b +=1
        b = 2
        d += c.center(2*n - 1, "-")
        d += '\n'
        c = ""
    return d
        

