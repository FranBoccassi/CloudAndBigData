#!/usr/bin/env python3

import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import string
import sys
import re
import csv

conf = SparkConf().setMaster('local').setAppName('tags_mas_usados.py')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

rdd=sc.textFile(sys.argv[1])
rdd.first() #quitamos la cabecera

tags=rdd.map(lambda x: x.lower().split(',')[1])

mapper=tags.map(lambda x: (x,1))
reducer=mapper.reduceByKey(lambda x,y:x+y)
hasattr(reducer, "toDF")
reducer.toDF().show()
ordenado=reducer.sortBy(lambda x: x[1]).collect()

file = open('tags_mas_usados.csv','w')

with file:
    writer = csv.writer(file)
    writer.writerows(ordenado)
