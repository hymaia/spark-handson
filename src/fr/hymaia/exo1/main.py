import pyspark.sql.functions as f
from pyspark.sql import SparkSession


def main():
    print("Hello world!")


def wordcount(df, col_name):
    return df.withColumn('word', f.explode(f.split(f.col(col_name), ' '))) \
        .groupBy('word') \
        .count()
