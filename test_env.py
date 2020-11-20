import os

environment = os.environ['ENVIRONMENT']
spark_driver_port = os.environ['SPARK_DRIVER_PORT']
spark_driver_host = os.environ['SPARK_DRIVER_HOST']
spark_blockmanager_port = os.environ['SPARK_BLOCKMANAGER_PORT']
spark_driver_bindaddress = os.environ['SPARK_DRIVER_BINDADDRESS']
print(f"ENVIRONMENT: {environment}")
print(f"SPARK_DRIVER_PORT: {spark_driver_port}")
print(f"SPARK_DRIVER_HOST: {spark_driver_host}")
print(f"SPARK_DRIVER_BINDADDRESS: {spark_driver_bindaddress}")
print(f"SPARK_BLOCKMANAGER_PORT: {spark_blockmanager_port}")

