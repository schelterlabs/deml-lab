## Task 1: Data Validation with Google TFX

The goal of this task is to use [Tensorflow Data Validation](https://www.tensorflow.org/tfx/guide/tfdv) to validate two sets of data files about products and ratings in the [data](data/) folder. 

We assume that all products data files are valid except for `products-data-3.tsv`. Additionally, we assume that `ratings-2.tsv` and `ratings-3.tsv` have anomalies.

Eyeballing the data should help you identify differences between the individual files. We ask you use **tfdv**  to infer a schema from the data, adjust the schema if necessary and ensure that your code correctly identifies the files with data anomalies. Use `python task1.py` to execute this task and implement your solution in [components/schema_validation.py]. Looking at this [test code](https://github.com/tensorflow/data-validation/blob/80809cd738fd1178f6c0334b0e4f4e644f445139/tensorflow_data_validation/anomalies/schema_test.cc) from Tensorflow might help you identify schema constraints that are helpful for this task.


## Task 2: Parallel Data Processing with Apache Beam

give schema of files

(1) join by identifier
(2) filter by (category == 'Kitchen' and rating >= 4) or (category == 'Jewelry' and rating == 5)
(3) group by category
(4) count num records per category
(5) Write category and counts into tab separated file category_counts.tsv-00000-of-00001, e.g.
Kitchen\t123
Jewelry\t456

## Task 3: Implement your own MapReduce Engine


Check MapReduceEngine.execute

(1) Run the map-phase: for each partition, transform each input record with f_r
(2) Run the shuffle-phase: create as many output partitions as we have reducers, all records with the same key must 
land in the same group in the same partition
(3) Run the reduce phase: apply f_r to every group in every partition

Your change does not need to be parallel or efficient

## Task 4: Parallel Linear Regression with MapReduce

use result_key() as the name for the model in the final result
