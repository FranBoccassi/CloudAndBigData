from pyspark.sql import SparkSession, functions as F
import sys
import csv
spark = SparkSession.builder.appName('Script1').getOrCreate()

path = "/home/mdpbelizon/Tags.csv"
path2 = "/home/mdpbelizon/miniQ.csv"
csvDF = spark.read.option("header","true").csv(sys.argv[1])
csvDF2 = spark.read.option("header","true").csv(sys.argv[2])


totalTags = csvDF.count()

#Preguntas sin responder
preguntasSinResponder = csvDF2.filter(csvDF2["ClosedDate"] != "NA").select("Id")
#Tags de las preguntas sin responder
tagsPSR = csvDF.join(preguntasSinResponder,csvDF["Id"] == preguntasSinResponder["Id"],'left_anti').select("Tag")
pairs = tagsPSR.withColumn("Count",F.lit(1))
countedPairs = pairs.groupby("Tag").count().orderBy("Count",ascending = 0).coalesce(1).write.csv('Test2.csv')


