from pyspark.sql import SparkSession, functions as F
import csv
spark = SparkSession.builder.appName('Script4').getOrCreate()


path = "/home/mdpbelizon/miniA.csv"
csvDF = spark.read.option("multiLine",True).option("escape", "\"").option("header",True).csv(path)
answerDF = csvDF.select('OwnerUserId','Score').groupBy('OwnerUserId').agg(F.avg('Score')).orderBy('avg(Score)',ascending = 0)
