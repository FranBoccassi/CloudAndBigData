from pyspark.sql import SparkSession, functions as F
import csv
import sys
spark = SparkSession.builder.appName('Script4').getOrCreate()


csvDF = spark.read.option("multiLine",True).option("escape", "\"").option("header",True).csv(sys.argv[1])
answerDF = csvDF.select('OwnerUserId','Score').groupBy('OwnerUserId').agg(F.avg('Score')).orderBy('avg(Score)',ascending = 0)
answerDF.coalesce(1).write.csv("Test3csv")
