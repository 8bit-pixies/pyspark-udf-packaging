
import os

def add_one_udf(udf_name):
    """
    This function provides a udf for pyspark!
    """
    # get the jar files as described from MANIFEST.in
    file_dir = os.path.abspath(os.path.dirname(__file__))
    jar_file = os.path.join(file_dir, 'src', 'simple-project_2.11-1.0.jar')

    try:
        from pyspark.sql.functions import first
        from pyspark.sql import SparkSession
        spark = SparkSession\
            .builder\
            .appName("simple_app")\
            .config("spark.jars", jar_file)\
            .getOrCreate()
        from pyspark.sql.types import DoubleType
        spark.udf.registerJavaFunction(udf_name, "featurestore.spark.udf.SimpleApp", DoubleType())
    except:
        raise Exception("It appears you have not started a spark session or pyspark is not accessible.")