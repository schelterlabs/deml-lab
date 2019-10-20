import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler, label_binarize
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from components.graph import pipeline_to_dataflow_graph

raw_data = pd.read_csv('adult-sample.csv', na_values='?')
data = raw_data.dropna()

labels = label_binarize(data['income-per-year'], ['>50K', '<=50K'])

nested_categorical_feature_transformation = Pipeline(steps=[
    ('impute', SimpleImputer(missing_values=np.nan, strategy='most_frequent')),
    ('encode', OneHotEncoder(handle_unknown='ignore'))
])

nested_feature_transformation = ColumnTransformer(transformers=[
    ('categorical', nested_categorical_feature_transformation, ['education', 'workclass']),
    ('numeric', StandardScaler(), ['age', 'hours-per-week'])
])

nested_pipeline = Pipeline([
  ('features', nested_feature_transformation),
  ('classifier', DecisionTreeClassifier())])

nested_model = nested_pipeline.fit(data, labels)

nested_graph = pipeline_to_dataflow_graph(nested_model)

assert len(nested_graph) == 7

vertices_by_name = {vertex.name:vertex for vertex in nested_graph}

assert 'features__numeric__age' in vertices_by_name.keys()
assert vertices_by_name['features__numeric__age'].parent_vertices == []

assert 'classifier' in vertices_by_name.keys()
assert len(vertices_by_name['classifier'].parent_vertices) == 4

assert 'features__categorical__education__encode' in vertices_by_name.keys()

vertex_to_inspect = vertices_by_name['features__categorical__education__encode']

assert len(vertex_to_inspect.parent_vertices) == 1
assert vertex_to_inspect.parent_vertices[0].name == 'features__categorical__education__impute'
