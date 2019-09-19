## Prerequisites

Update your git repository and setup the virtual environments for this assignment analogously to how you did it for the lab exercises.

The assignment consists of three independent tasks. Each task features a python file to execute. In order to fullfil the assignment, you have to **implement python code in the files in the [components](components/) folder**. **Do not edit other files, especially the task files**.

## Task 1

You can execute this task via ```python task1.py```. The goal of this task is to implement a few constraints for data validation defined in the file [components/constraints.py](components/constraints.py). Each constraint applies to a pandas dataframe and tests certain conditions on the contained data (or a specific column)

 * `HasAtLeastNumRecords`: checks that the dataframe has at least a given number of records
 * `NotNull`: checks that a column contains no null values
 * `HasNumDistinctValues`: checks that a columns number of distinct values is in a given range (including the min/max)
 * `IsInRange`: checks that a columns values are in a given range (including the min/max)
 * `And`: checks that all of the supplied constraints is satisfied
 * `Or`: checks that at least one of the supplied constraints is satisfied


## Task 2

You can execute this task via ```python task2.py```. The goal of this task is to implement an ML-based missing value imputer as an estimator/transformer in scikit learn in the file [components/learned_imputer.py](components/learned_imputer.py). 

You will work on a pandas dataframe, and your goal is to learn a model to impute missing values for the `target_column` given the values from the other columns of the dataframe. The choice of features and model is up to you. 

The model will be learned in the `fit` method of the class. For the sake of simplicity, you can assume that the dataframe only contains text columns. In the `transform` method of the class, your learned imputer should fill in missing values for the `target_column`. You can run the tests for your imputer via ```python task2.py```, you should try to achieve an accuracy greater than 0.75.
