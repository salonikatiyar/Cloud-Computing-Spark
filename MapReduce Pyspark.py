#!/usr/bin/env python
# coding: utf-8

# # To implement a Map/Reduce program on PySpark

# In[194]:


#import packages
from pyspark import SparkFiles
import re
from pyspark import SparkConf, SparkContext
import sys
from pyspark.sql.functions import regexp_replace
import py4j
from pyspark.sql.functions import lower


# In[195]:


#read text file
textFile = open("C:/Users/SALONI/Documents/Semester 4/Cloud Computing/Assignment 1/input.txt")


# In[196]:


textFile


# In[197]:


#entry point for manipulating data
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)


# In[198]:


#data manipulation
#removing digits and punctuations 
result = re.sub(r'[\d+]', " ", textFile.read())
new_result = re.sub(r'[^\w\s]', " ", result)
#converting to lower-case
with open('text_result.txt',"w") as f:
    f.write(new_result.lower())


# In[220]:


#rdd operations
rddfile = spark.sparkContext.textFile("text_result.txt")
rddfile


# In[221]:


rddfile.take(10)


# In[222]:


rddfile.collect()


# In[249]:


import itertools


# In[257]:


final = (
    rddfile.filter(lambda x: x != "")
        .map(lambda x: x.split(" "))
        .flatMap(lambda x: itertools.combinations(x, 2))
        .filter(lambda x: x[0] != "")
        .map(lambda x: (x, 1))
        .reduceByKey(lambda x, y: x + y)
)


# In[258]:


final


# In[259]:


#saving the output
final.saveAsTextFile('Desktop/output.txt')


# In[ ]:




