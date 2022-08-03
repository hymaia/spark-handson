import pyspark.sql.functions as f
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("exo4").master("local[*]").getOrCreate()

def main():
    print("Hello world!")

