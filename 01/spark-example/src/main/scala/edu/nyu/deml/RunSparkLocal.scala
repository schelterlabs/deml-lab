package edu.nyu.deml

import org.apache.spark.sql.SparkSession

object RunSparkLocal extends App {

  case class Item(id: Long, productName: String, description: String, priority: String, numViews: Long)

  withSpark { session =>

    val rdd = session.sparkContext.parallelize(Seq(
      Item(1, "Thingy A", "awesome thing.", "high", 0),
      Item(2, "Thingy B", "available at http://thingb.com", null, 0),
      Item(3, null, null, "low", 5),
      Item(4, "Thingy D", "checkout https://thingd.ca", "low", 10),
      Item(5, "Thingy E", null, "high", 12)),
      numSlices = 2)

    val data = session.createDataFrame(rdd)

    val count = data.count()

    println(s"$count items found.")
  }





  def withSpark(func: SparkSession => Unit): Unit = {

    val session = SparkSession.builder()
      .master("local")
      .appName("test")
      .config("spark.ui.enabled", "false")
      .config("spark.sql.shuffle.partitions", 2.toString)
      .getOrCreate()
    session.sparkContext.setCheckpointDir(System.getProperty("java.io.tmpdir"))

    try {
      func(session)
    } finally {
      session.stop()
      System.clearProperty("spark.driver.port")
    }
  }

}
