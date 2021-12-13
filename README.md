# CloudAndBigData

___

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
This repository contains 2 main directories and 2 more for the web and imagenes obtained:
- assets: all the necessary files to run the web.
- images: all the images obtained for visual representation.
- reducedDatasets: all the .csv files saved obtained by the results of the scripts on dataset's.
- scripts: all the pySpark scripts used for recover the data analisis.

## How to prepare the VM:
These will be the recipe for prepare a linux/ubuntu OS-VM instance with Spark integrated, described as command lines without use gCloud UI.

> Get the VM prepare

- First, to create the VM instance type this sentence in the gCloud shell:
```
gcloud compute instances create spark-local --project=platinum-snow-327612 --zone=europe-west6-a --machine-type=n1-highcpu-4
```
Then you will get this result message:
![created](https://user-images.githubusercontent.com/48984072/145902197-764f7d6b-0f8d-43eb-9033-091120c47a3c.jpg)

So, now it's time to begin the use of our VM instance, for that type in gCloud shell
```
gcloud beta compute ssh --zone "europe-west6-a" "spark-local"  --project "platinum-snow-327612"
```

- Then, install java...
```
sudo apt install default-jre
```
...then test the version with:
```
java -version
```

- And, install spark, with the following lines...
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
...and test Spark:
```
spark-submit /usr/local/spark/examples/src/main/python/pi.py 10
```

Clear all with `clear`

## How to use this tool:
These will be the recipe for test our code, described as command lines inside the VM SSH.

> Here starts the project software



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
