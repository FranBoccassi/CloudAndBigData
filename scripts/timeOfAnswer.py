#En este script vamos a mostrar el tiempo medio de respuesta de una pregunta de stackoverflow(es un sitio de preguntas y respuestas para programadores profesionales y 
#aficionados) según los tags que ésta pregunta contenga. Con esto podremos saber en caso de hacer una pregunta con tags el tiempo aproximado que tardarán en respondernos, 
#y hacernos una idea de según el tiempo de respuesta que conocimiento tienen más los usuarios de esta web de preguntas.
#Notaciones: Se calculará la media con la primera respuesta subida, independientemnete de la puntuación de ésta. El objetivo es conocer en que está más especializado los 
#usuarios de esta web, por eso se coge la respuesta con la fecha menor.
#Sabemos que la primera respuesta registrada es del 01-08-2008 a las 14:45:37, esta fecha será nuestro punto de referencia.

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row, Column, SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import *
import pyspark.sql.functions as f
import datetime

import string
import re
import sys
import shutil
import csv

conf = SparkConf().setAppName('timeOfAnswer')
sc = SparkContext(conf = conf)

# Create Spark session
spark = SparkSession.builder \
    .appName('timeOfAnswer') \
    .master('local') \
    .getOrCreate()

# Setup hadoop fs configuration for schema gs://, para realizar bien la conexión con el cloud storage
conf = spark.sparkContext._jsc.hadoopConfiguration()
conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
conf.set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")  #Comprobar si es necesario

try:
    shutil.rmtree('timeOfAnswer.csv')
except OSError as e:
    print("No existe el directorio")

file = open('timeOfAnswer.csv', 'w')

questionDF = spark.read.option('Header', 'true').csv(sys.argv[1]).select('Id', f.translate(f.col('CreationDate'), "TZ", "  ").alias('CreationDate'))\
            .withColumn('QuestionDate', to_timestamp("CreationDate"))  

answerDF = spark.read.option('Header', 'true').csv(sys.argv[2]).select(f.translate(f.col("CreationDate"), "TZ", "  ").alias('AnswerDate'), 'ParentId')\
            .withColumn('AnswerDate', to_timestamp('AnswerDate')).groupBy('ParentId').agg(min('AnswerDate').alias('AnswerDate'))

tagsDF = spark.read.option('Header', 'true').csv(sys.argv[3]).select(col('Id').alias('QuestionId'),'Tag')

df = questionDF.join(answerDF, questionDF.Id == answerDF.ParentId, 'inner').join(tagsDF, questionDF.Id == tagsDF.QuestionId, 'inner')\
        .withColumn('Difference', col('AnswerDate').cast('long') - col('QuestionDate').cast('long')).groupBy('Tag').agg(avg('Difference')).alias('Average time(secs)')

df.coalesce(1).write.csv('FileTimeOfAnswer.csv')

