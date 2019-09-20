import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from components.trainer import create_pipeline, create_label_encoder, train_model_with_crossvalidation
from sklearn.metrics import roc_auc_score

# This task defines how we want to train a supervised model for some given data
class LearningTask:
    def __init__(self,
                 target_column,
                 categorical_columns,
                 numeric_columns,
                 textual_columns,
                 learning_algorithm,
                 num_folds,
                 hyperparam_grid):
        self.target_column = target_column
        self.categorical_columns = categorical_columns
        self.numeric_columns = numeric_columns
        self.textual_columns = textual_columns
        self.learning_algorithm = learning_algorithm
        self.num_folds = num_folds
        self.hyperparam_grid = hyperparam_grid


# We execute the learning tasks using the methods defined in trainer.py
def execute_task(task, data, current_seed):

    # We split
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=current_seed)

    # We create the pipeline for our task
    pipeline = create_pipeline(task)

    # We obtain the fitted label encoder
    label_encoder = create_label_encoder(task, train_data)

    # We invoke the model training
    model = train_model_with_crossvalidation(task, pipeline, label_encoder, train_data, current_seed)

    # We compute the AUC of the model
    y_true = label_encoder.transform(test_data[task.target_column])
    y_pred = model.predict_proba(test_data)[:, 0]
    auc_score = roc_auc_score(y_true, y_pred)

    if auc_score < 0.5:
        auc_score = 1.0 - auc_score

    return auc_score


# We evaluate our model on income data
income_data = pd.read_csv('adult-sample.csv')

# We run several experiments with different random seeds
for seed in [42, 12345]:
    
    task1 = LearningTask(
        target_column='income-per-year',
        categorical_columns=['workclass', 'occupation', 'marital-status'],
        numeric_columns=['age', 'capital-gain', 'capital-loss'],
        textual_columns=[],
        learning_algorithm=SGDClassifier(loss='log', random_state=seed),
        num_folds=4,
        hyperparam_grid={'penalty': ['l2', 'l1'], 'alpha': [0.01, 0.001, 0.0001]})

    auc1 = execute_task(task1, income_data, seed)
    print("AUC %s for task1 with seed %s" % (auc1, seed))

    task2 = LearningTask(
        target_column='income-per-year',
        categorical_columns=['occupation'],
        numeric_columns=['age'],
        textual_columns=[],
        learning_algorithm=SGDClassifier(loss='log', random_state=seed),
        num_folds=4,
        hyperparam_grid={'penalty': ['l2', 'l1'], 'alpha': [0.01, 0.001, 0.0001]})

    auc2 = execute_task(task2, income_data, seed)
    print("AUC %s for task2 with seed %s" % (auc2, seed))

    task3 = LearningTask(
        target_column='income-per-year',
        categorical_columns=['occupation'],
        numeric_columns=['age'],
        textual_columns=[],
        learning_algorithm=RandomForestClassifier(random_state=seed),
        num_folds=4,
        hyperparam_grid={'n_estimators': [10, 100, 1000]})

    auc3 = execute_task(task3, income_data, seed)
    print("AUC %s for task3 with seed %s" % (auc3, seed))

    task4 = LearningTask(
        target_column='sex',
        categorical_columns=['workclass', 'occupation', 'marital-status', 'income-per-year'],
        numeric_columns=['age', 'capital-gain', 'capital-loss'],
        textual_columns=[],
        learning_algorithm=SGDClassifier(loss='log', random_state=seed),
        num_folds=4,
        hyperparam_grid={'penalty': ['l2', 'l1'], 'alpha': [0.01, 0.001, 0.0001]})

    auc4 = execute_task(task4, income_data, seed)
    print("AUC %s for task4 with seed %s" % (auc4, seed))

