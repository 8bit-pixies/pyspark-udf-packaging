

package featurestore.spark.udf

import org.apache.spark.sql.api.java.UDF1

class SimpleApp extends UDF1[Double, Double] {

  override def call(number:Double): Double = {
    number + 1.0
  }
}
