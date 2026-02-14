from pyspark import pipelines as dp

@dp.table(name="catalog2_we47.schema2_we47.silver_shipmentsDLTST1")
def streaming_load():
  df1=spark.readStream.table("lakehousecat1.deltadb.drugstbl_merge")
  return df1
#Few important understanding we need to get out of this program (most of our DP learning will be over if you do this..)
#1. How to write a declarative program rather than imperative - We used pipelines and decorator
#2. How to handle streaming data ingestion (only inserted) from the source (fact table/transactions/events tables) - 
#  a. Source table will be collected incremental with only inserted data (if i use readStream.table function)
#  b. Target table (stream table) will allow insert with inserted/newly added data from the source (it will not engage updated/delete in the target)

#This pipeline creates a streaming DLT table that incrementally ingests data using Structured Streaming. By default, it supports append-only ingestion. For handling updates and deletes, CDC with APPLY CHANGES must be enabled.
