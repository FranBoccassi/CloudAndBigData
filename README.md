# CloudAndBigData

___
### StackOverflow Questions & Answers Analysis
###### website: [show the web][WEB]
[WEB]: https://franboccassi.github.io/CloudAndBigData/#
[Portada]: images/prosus-compra-stack-overflow.jpg

![stackOverflow][Portada]
___

## Introduction

StackOverflow Questions & Answers is a project that tries to analyze the efficiency of the most popular server among programmers, which has a very good reputation.

This analysis tries to demonstrate to what extent it is true that it is one of the best performing servers in the world.

### Description of the problem

We often find ourselves with doubts about how to make certain code in programming, we tend to think that why are we going to "reinvent the wheel" since many of the things we need to do when we develop a programming project, is based on reusing parts of code with different functions, these are usually the subject of our doubts, how those who have already done it will have done it, how it will be the most efficient way ... To all this in most cases we find support in StackOverflow.

### Need for Big Data

Being able to see each and every one of the questions along with their respective answers, reaches an excessively large size, due to the fact that it brings together a community on a world scale. In addition, it serves as a backup for all types of programming languages. For this reason, we have made scripts that facilitate data collection and also generate different contrasts of information, for this we use a Google Cloud virtual machine instance with 4vCPU and 3.6Gb of memory.

### Solution

For the developed solution we have obtained the most up-to-date dataset's, on these we carry out the following processes: filter, analyze, save and represent the information obtained; according to the different aspects that we have taken into account, such as: the average response time, the most frequent tags, that is, the most used languages ​​and those tags that have not obtained a specific solution.

Which helps us in the first place, for example, to clarify the evidence of the number of unsolved questions.

Here we leave the link for the datasets that we have used, they are too wide to upload to GitHub:
https://www.kaggle.com/stackoverflow/stacksample

## Dataset:
With a total of 3.6Gb, this dataset with the text of 10% of questions and answers from the Stack Overflow programming Q&A website, provides three organized tables:

- Questions: contains the title, body, creation date, closed date (if applicable), score, and owner ID for all non-deleted Stack Overflow questions whose Id is a multiple of 10.
- Answers: contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.
- Tags: contains the tags on each of these questions.

## Repository contents:
This repository contains 2 main directories about BigData project and 2 more about web and images obtained, in order they are:
- assets: all the necessary files to run the web.
- images: all the images obtained for visual representation.
- reducedDatasets: all the .csv files saved obtained by the results of the scripts on dataset's.
- scripts: all the pySpark scripts used for recover the data analisis.

## How to prepare the VM:
These will be the recipe for prepare a linux/ubuntu OS-VM instance with Spark integrated, 
described as command lines on **gCloud shell**.

> Get the VM prepare

  **1.** First, to **create the VM** instance type this sentence in the gCloud shell:
```
gcloud compute instances create spark-local --project=platinum-snow-327612 --zone=europe-west6-a --machine-type=n1-highcpu-4
```
Then you will get this result message:
![created](https://user-images.githubusercontent.com/48984072/145902197-764f7d6b-0f8d-43eb-9033-091120c47a3c.jpg)

So, now it's time to begin the use of our VM instance, for that type in gCloud shell to use the **SSH UI**
```
gcloud beta compute ssh --zone "europe-west6-a" "spark-local"  --project "platinum-snow-327612"
```

  **2.** Then, **install java**...
```
sudo apt install default-jre
```
...then test the version with:
```
java -version
```

  **3.** And, **install spark**, with the following lines...
```
curl -O https://ftp.cixug.es/apache/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
tar xvf spark-3.1.2-bin-hadoop3.2.tgz
sudo mv spark-3.1.2-bin-hadoop3.2 /usr/local/spark
```
...need to run is to add spark path to the user profile, like these...
```
PATH="$PATH:/usr/local/spark/bin"
source ~/.profile
```
...then test Spark:
```
spark-submit /usr/local/spark/examples/src/main/python/pi.py 10
```

Clear all with `clear` and type `exit`.

##### In this project we have developed 4 scripts whose we encontered very interesting to show main statistics about this tool.

## How to use this tool: timeOfAnswer.py
These will be the recipe for test our code, described as command lines inside the VM SSH.

> Here starts the project software
- Make sure you have set correctly the PATH.

**1.** With pySpark running in SHH of the spark VM, for download the connector:
```
wget https://repo1.maven.org/maven2/com/google/guava/guava/30.1-jre/guava-30.1-jre.jar

mv /usr/local/spark/jars/guava-14.0.1.jar /usr/local/spark/jars/guava-14.0.1.jar.bk

cp guava-30.1-jre.jar /home/$USER/.local/lib/python3.7/site-packages/pyspark/jars
```

**2.** For created the **bucket** for test and save files in our cloud storage:
```
BUCKET=gs://<user>/stackOverFlow
BUCKET=gs:<BUCKET>
```
And, submit there **.csv files** downloaded from the Kaggle website.

**3.** To execute the **timeOfAnswer.py** script that uses the three *DataSets* that compose this project:
```
spark-submit --packages com.google.cloud.bigdataoss:gcs-connector:hadoop3-2.2.0 timeOfAnswer.py $BUCKET/Questions.csv $BUCKET/Answers.csv $BUCKET/Tags.csv
```

## How to use this tool: In general terms
> You can use this line script changing the **.py** file and the **datasets** included:
```
spark-submit --packages com.google.cloud.bigdataoss:gcs-connector:hadoop3-2.2.0 <script.py> $BUCKET/<dataset01>.csv $BUCKET/<dataset02>.csv ...
```

## Running scripts in different Clusters check

**1.** From gCloud shell, create **cluster** with 2 workers and 4 cores
```
gcloud dataproc clusters create stackoverflow-cluster --enable-component-gateway --region europe-west6 --zone europe-west6-b --master-machine-type n1-standard-4 --master-boot-disk-size 50 --num-workers 2 --worker-machine-type n1-standard-4 --worker-boot-disk-size 50 --image-version 2.0-debian10
```
**2.** Once created, we access their virtual instances and get into the **master node stackoverflow-cluster-m** 
![cluster 2w 4c](https://user-images.githubusercontent.com/48984072/145990960-d1eaf269-f481-4aad-9904-dccc80f2553a.png)

**3.** We test it with the two following scripts, accessing from cloud storage and check if it runs well: 

> Checking timeOfAnswer.py
```
BUCKET=gs:<BUCKET>
spark-submit $BUCKET/timeOfAnswer.py $BUCKET/Questions.csv $BUCKET/Answers.csv $BUCKET/Tags.csv
```
- With 2 worker and 4 cores this takes: real 23.381secs. / user 32.883secs. / sys 1.54secs.
- And, with 4 workers and 4 cores this takes: real 24.162secs. / user 34.667secs. /  sys 1.541secs.

> Checking script3.py
```
BUCKET=gs:<BUCKET>
spark-submit $BUCKET/script3.py $BUCKET/Answers.csv
```
- With 2 worker and 4 cores this takes: real 20.022secs. / user 26.022secs. / sys 1.433secs.
- And, with 4 workers and 4 cores this takes: real 19.108secs. / user 25.541secs. /  sys 1.357secs.

![Bytes de disco](https://user-images.githubusercontent.com/48984072/145996957-896a1f12-556e-4d87-bea6-f5d0a3115a8a.png)
![Operaciones de disco](https://user-images.githubusercontent.com/48984072/145996959-4025b847-12f6-41c6-b7e0-757d1d3fcf8b.png)
![Paquetes de red](https://user-images.githubusercontent.com/48984072/145996961-e080ad6a-ecaa-40d8-adc5-4c73fc7462fd.png)
![Uso de CPU](https://user-images.githubusercontent.com/48984072/145996964-9ca697c5-8fba-419f-a2e9-31fbe385552f.png)

## Bottom line:
There a lot of questions that may not have a clear solution.
Possible improvements:
- Make an interactive-integrated tool to have a clear visibility of actuality.
- Make more interesting solutions like clasification about users with highest score.

## Tools used:
- Google Cloud - used for VM instance with linux SO and pySpark.
- Spark - to map and reduce the data.
- Excel - to make representative diagrams of the result.

## Team formation:
- adgarr01@ucm.es Adrian Garrido Blazquez -- Software Engineering
- franbocc@ucm.es Francisco Boccassi -- Software Engineering
- jorgelas@ucm.es Jorge Lasheras Martín -- Software Engineering
- manupacr@ucm.es Manuel Pérez Belizón -- Informatics Engineering
- pablocub@ucm.es Pablo Cubells -- Video Game Development
