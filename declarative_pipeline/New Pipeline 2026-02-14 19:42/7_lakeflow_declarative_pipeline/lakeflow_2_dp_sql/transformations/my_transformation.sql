CREATE OR REFRESH STREAMING TABLE catalog2_we47.schema2_we47.silver_shipmentsDLT_ST_SQL
AS
SELECT *
FROM STREAM(lakehousecat1.deltadb.drugstbl_merge);