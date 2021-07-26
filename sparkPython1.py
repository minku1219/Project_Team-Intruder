#!/usr/bin/python3

from pyspark import SparkContext

# connecting sparkcontext with spark master ..

sc=SparkContext("local","app_first")
# now sc is same as pyspark sc
firstRDD=sc.textFile('/tmp/data.txt')
RDD=firstRDD.collect()
# second method creating data inside python only 
#data1=["hello","this","is","python","power"]
# loading data from a list

transform1=sc.parallelize(RDD)
# now we can do some action 

action1=transform1.count()

#printing
print("Number of RDD element ",action1)

