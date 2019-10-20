import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler, label_binarize
from sklearn.compose import ColumnTransformer

from components.graph import pipeline_to_dataflow_graph

raw_data = pd.read_csv('adult-sample.csv', na_values='?')
data = raw_data.dropna()

labels = label_binarize(data['income-per-year'], ['>50K', '<=50K'])

feature_transformation = ColumnTransformer(transformers=[
    ('categorical', OneHotEncoder(handle_unknown='ignore'), ['education', 'workclass']),
    ('numeric', StandardScaler(), ['age', 'hours-per-week'])
])

income_pipeline = Pipeline([
  ('features', feature_transformation),
  ('classifier', DecisionTreeClassifier())])

income_model = income_pipeline.fit(data, labels)

income_graph = pipeline_to_dataflow_graph(income_model)


assert len(income_graph) == 5

steps_without_parent = set(['features__categorical__education',
                            'features__categorical__workclass',
                            'features__numeric__age',
                            'features__numeric__hours-per-week'])

for vertex in income_graph:
    if vertex.name in steps_without_parent:
        assert len(vertex.parent_vertices) == 0
        if 'categorical' in vertex.name:
            assert vertex.operation == 'OneHotEncoder'
        else:
            assert vertex.operation == 'StandardScaler'
    else:
        assert len(vertex.parent_vertices) == 4
        assert vertex.name == 'classifier'
