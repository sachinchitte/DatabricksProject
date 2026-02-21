from pyspark import pipelines as dp
from pyspark.sql.functions import *
@dp.table(name="bronze_staff_data2")
def bronze_staff_data():
    #base_path is defined in configuration(setting)
    base_path1 = spark.conf.get("base_path") 
    return (spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "csv")
            .option("inferColumnTypes", "true")
            .option("cloudFiles.schemaEvolutionMode","addNewColumns")
            .load(f"{base_path1}/staff"))


@dp.table(name="bronze_geotag_data2")
def bronze_geotag_data():

    return (
        spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "csv")
            .option("inferColumnTypes", "true")
            .load("/Volumes/catalog2_we47/medallion_dlt/dlt/datalake/geotag/")
    )


@dp.table(name="bronze_shipments_data2")
def bronze_shipments_data():

    return (
        spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "json")
            .option("inferColumnTypes", "true")
            .option("multiLine", "true")
            .load("/Volumes/catalog2_we47/medallion_dlt/dlt/datalake/shipment/")
            .select(
                "shipment_id",
                "order_id",
                "source_city",
                "destination_city",
                "shipment_status",
                "cargo_type",
                "vehicle_type",
                "payment_mode",
                "shipment_weight_kg",
                "shipment_cost",
                "shipment_date"
            )
    )
