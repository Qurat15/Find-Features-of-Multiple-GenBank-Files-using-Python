#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[29]:


import glob
from Bio import SeqIO
from collections import Counter
import pandas as pd
import os


# # Folder Path

# In[15]:


file_directory = '/home/qurat-ul-ain/Downloads/sequences'


# #  Accessing files name using glob

# In[16]:


gfiles = glob.glob("%s/*.gb"%file_directory)


# In[17]:


gfiles


# In[7]:


gfiles[0]


# #  Used Above imported libraries to store features of GenBank files into .csv file

# In[21]:


def count_features(gfile):
    genbank_object=SeqIO.read(gfile,"gb")
    features=genbank_object.features
    feature_types=[feature.type for feature in features]
    feature_count=Counter(feature_types)
    print('features have been counted')
    
    dataframe=pd.DataFrame(feature_count.items(),columns=['Feature','Count'])
    
    directory,filename=os.path.split(gfile)
    filename=filename.strip('.gb')
    
    basedir='/home/qurat-ul-ain/Downloads'
    
    outputfile='%s/%s.csv'%(basedir,filename)
    
    dataframe.to_csv(outputfile,index=False)
    
    print('Count data has been saved')


# #  Loop to access each file one by one

# In[22]:


for gfile in gfiles:
    count_features(gfile)

