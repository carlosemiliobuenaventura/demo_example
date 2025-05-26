# Databricks notebook source
from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.profile("isp_new_env_demo").getOrCreate()

df = spark.read.table("samples.nyctaxi.trips")
df.show(500000)

# COMMAND ----------

df = spark.read.option('asOfVersion', 4) \
    .table("isp_demo_carlos.session_2.employee")
df.show(5)
