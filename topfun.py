
# coding: utf-8

# In[6]:

def is_hill(seq):
    from string import ascii_letters
    seq_list = list(seq)
    number_list= []
    index = 0
    c = 0
    if (len(seq)==1 or len(seq)==2):
        return False
    for x in seq: 
        n= ord(x)
        number_list.append(n)
    for numbers in number_list[0:len(seq)//2]:
        if (number_list[index] < number_list[index + 1]):
            c = c
            index+=1
        else:
            c+=1
    for numbers in number_list[len(seq)//2:len(seq)-1]:
        if (number_list[index]>number_list[index+1]):
            c=c
            index+=1
        else:
            c+=1
    if (c==0):
        return True
    else: 
        return False


# In[7]:

def is_plain(seq):
    from string import ascii_letters
    seq_list = list(seq)
    number_list = []
    index = 0
    c = 0
    if (len(seq) == 1):
        return False
    for x in seq:
        n = ord(x)
        number_list.append(n)
    for numbers in number_list[0:len(seq)-1]:
        if (number_list[index] == number_list[index+1]):
            c=c
            index+=1
        else: 
            c+=1
    if (c==0):
        return True
    else: 
        return False


# In[8]:

def is_ramp(seq): 
    from string import ascii_letters
    seq_list = list(seq)
    number_list= []
    index = 0
    c = 0
    digit_list= [1,2,3,4,5,6,7,8,9,0]
    if (seq_list[0] not in digits):
        if (len(seq)==1):
            return False
        for x in seq:
            n=ord(x)
            number_list.append(n)
        for numbers in number_list[0:len(seq)-1]:
            if (number_list[index] < number_list[index+1]):
                c = c 
                index+=1
            else:
                c+=1
    else:
        if (len(seq)==1):
            return False
        for x in seq: 
            number_list.append(n)
        for numbers in number_list[0:len(seq)-1]:
            if (number_list[index] < number_list[index+1]):
                c = c
                index+=1
            else:
                c+=1
    if (c==0):
        return True
    else: 
        return False


# In[9]:

def is_slope(seq):
    from string import ascii_letters
    seq_list = list(seq)
    number_list= []
    index = 0
    c = 0
    digit_list= [1,2,3,4,5,6,7,8,9,0]
    if (seq_list[0] not in digits):
        if (len(seq)==1):
            return False
        for x in seq:
            n=ord(x)
            number_list.append(n)
        for numbers in number_list[0:len(seq)-1]:
            if (number_list[index] > number_list[index+1]):
                c = c 
                index+=1
            else:
                c+=1
    else:
        if (len(seq)==1):
            return False
        for x in seq: 
            number_list.append(n)
        for numbers in number_list[0:len(seq)-1]:
            if (number_list[index] > number_list[index+1]):
                c = c
                index+=1
            else:
                c+=1
    if (c==0):
        return True
    else: 
        return False


# In[15]:

def is_valley(seq):
    from string import ascii_letters
    seq_list = list(seq)
    number_list = []
    index = 0
    c = 0
    if (len(seq)==1 or len(seq)==2):
        return False
    for x in seq:
        n=ord(x)
        number_list.append(n)
    for numbers in number_list[0:len(seq)//2]:
        if (number_list[index] > number_list[index + 1]):
            c = c
            index+=1
        else:
            c+=1
    for numbers in number_list[len(seq)//2:len(seq)-1]:
        if (number_list[index]<number_list[index+1]):
            c=c
            index+=1
        else:
            c+=1
    if (c==0):
        return True
    else: 
        return False


# In[ ]:



