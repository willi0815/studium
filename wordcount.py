from pyspark import SparkConf, SparkContext
from operator import add

conf = SparkConf().setAppName("WordCount").setMaster("local[3]")
sc = SparkContext(conf=conf)
rddText = sc.textFile("t8.shakespeare_mod.txt")
wordsCounts = rddText \
    .flatMap(lambda line: line.split(' ')) \
    .map(lambda word: word.lower()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(add)

wordsList = wordsCounts.takeOrdered(25, key=lambda x: -x[1])
wordsList.pop(0) 
i=1
for count_item in wordsList:
    print("{}. {} - {}".format(i, count_item[0], count_item[1]))
    i=i+1
