#!/usr/bin/python

from pyspark  import  SparkContext

sc=SparkContext("local","App_first")

filename="file:///tmp/data.txt"
load_file=sc.textFile(filename).cache()

numacount=load_file.filter(lambda s: 'a' in s).count()
numbcount=load_file.filter(lambda s: 'b' in s).count()

print  ("line with a: ",numacount)
print  ("line with b: ",numbcount)

