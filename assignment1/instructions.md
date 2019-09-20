## Prerequisites

Update your git repository and setup the virtual environment for this assignment analogously to how you did it for the lab exercises.

The assignment consists of three independent tasks. Each task features a python file to execute. Note that the execution might result in errors if you did not implement the require code yet. In order to fulfill the assignment, you have to **implement python code in the files in the [components](components/) folder**. **Do not edit other files, especially the task files**.

## Task 1: Data Validation

You can execute this task via ```python task1.py```. The goal of this task is to implement a few constraints for data validation defined in the file [components/constraints.py](components/constraints.py). Each constraint applies to a pandas dataframe and tests certain conditions on the contained data (or a specific column)

 * `HasAtLeastNumRecords`: checks that the dataframe has at least a given number of records
 * `NotNull`: checks that a column contains no null values
 * `HasNumDistinctValues`: checks that a columns number of distinct values is in a given range (including the min/max)
 * `IsInRange`: checks that a columns values are in a given range (including the min/max)
 * `And`: checks that all of the supplied constraints is satisfied
 * `Or`: checks that at least one of the supplied constraints is satisfied


## Task 2: A custom Estimator/Transformer for Missing Value Imputation

You can execute this task via ```python task2.py```. The goal of this task is to implement an ML-based missing value imputer as an estimator/transformer in scikit learn in the file [components/learned_imputer.py](components/learned_imputer.py). 

You will work on a pandas dataframe, and your goal is to learn a model to impute missing values for the `target_column` given the values from the other columns of the dataframe. The choice of features and model is up to you. 

The model will be learned in the `fit` method of the class. For the sake of simplicity, you can assume that the dataframe only contains text columns. In the `transform` method of the class, your learned imputer should fill in missing values for the `target_column`. 

As an example, we will impute the category of a product given its `review` and `title` with data taken from [products.csv](products.csv). You can run the tests for your imputer via ```python task2.py```, you should try to achieve an accuracy greater than 0.75.

## Task 3: Declarative Model Training

You can execute this task via ```python task3.py```. In this task, we will implement a very simple "AutoML" system for supervised learning. You are given data in the form of a pandas dataframe, as well as a [`LearningTask`](task3.py#L9) which describes which column values we want to predict (`target_column`) and which columns we want to use as features (`categorical_columns`, `numeric_columns`, `textual_columns`). Additional, you are provided with the `learning_algorithm` to use, as well as with the number of folds `num_folds` and a hyperparameter grid for `hyperparam_grid` for grid search.

The goal is to implement the following methods in [components/trainer.py](components/trainer.py) to conduct the model training invoked by ```python task3.py```:
 
 * `create_pipeline(task)`: Generate a sklearn pipeline for training a model corresponding to the task 
 * `create_label_encoder(task, training_data)`: return a fitted [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) for the `target_column`
 * `train_model_with_crossvalidation(task, pipeline, label_encoder, training_data, seed)`: train the model (e.g. the pipeline defined earlier) using k-fold cross-validation

The tasks file defines different tasks to predict certain columns of a sample of [income data](adult-sample.csv) and should result in an AUC of about 0.8 in most of the cases.
