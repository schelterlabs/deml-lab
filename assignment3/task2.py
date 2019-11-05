from sklearn.preprocessing import Binarizer
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

from components.graph import pipeline_to_dataflow_graph

# EXAMPLE 1
data = [[13.0, 0.0, 1.0],
        [27.0, 1.0, 0.0]]

binarizer_pipeline = Pipeline([
    ('binarization', Binarizer(threshold=5.0))
])

binarizer_model = binarizer_pipeline.fit(data)
binarizer_graph = pipeline_to_dataflow_graph(binarizer_model)

assert len(binarizer_graph) == 1

vertex = binarizer_graph[0]

assert len(vertex.parent_vertices) == 0
assert vertex.name == 'binarization'
assert vertex.operation == 'Binarizer'


# EXAMPLE 2
iris_dataset = load_iris()

iris_pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('classifier', DecisionTreeClassifier())])

iris_model = iris_pipeline.fit(iris_dataset.data, iris_dataset.target)
iris_graph = pipeline_to_dataflow_graph(iris_model, parent_vertices=[])

assert len(iris_graph) == 2

for vertex in iris_graph:
    if vertex.name == 'scaler':
        assert len(vertex.parent_vertices) == 0
    if vertex.name == 'classifier':
        assert len(vertex.parent_vertices) == 1
        assert vertex.parent_vertices[0].operation == 'StandardScaler'
