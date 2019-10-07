from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import GridSearchCV


def create_pipeline(task):
    feature_transformation = ColumnTransformer(transformers=[
        ('categorical_features', OneHotEncoder(handle_unknown='ignore'), task.categorical_columns),
        ('scaled_numeric_features', StandardScaler(), task.numeric_columns)
    ])

    pipeline = Pipeline([
        ('features', feature_transformation),
        ('classifier', task.learning_algorithm)])

    return pipeline


def create_label_encoder(task, training_data):
    encoder = LabelEncoder()
    encoder.fit(training_data[task.target_column])

    return encoder




def train_model_with_crossvalidation(task, pipeline, label_encoder, training_data, seed):

    new_key = {}
    for i in task.hyperparam_grid.items():
        new_key.update({'classifier__'+i[0]:i[1]})


    grid_search = GridSearchCV(estimator=pipeline,
                               param_grid=new_key,
                               scoring='accuracy',
                               cv=task.num_folds
                               )
    grid_search.fit(training_data, label_encoder.transform(training_data[task.target_column]))

    return grid_search






