from sklearn.datasets import make_regression
from components.mapreduce import MapReduceEngine
from components.linear_regression import f_m, f_r, result_key
from utils import to_partitions
import numpy as np

# Generate an artifical regression problem
X, y = make_regression(n_samples=100, n_features=5, random_state=42)

# Generate partitioned input data
partitions = to_partitions(X, y, num_partitions=10, num_records_per_partition=10)

# Run the computation using our self-coded mapreduce engine
engine = MapReduceEngine(f_m=f_m, f_r=f_r, num_reducers=2)
results = engine.execute(partitions)

# Retrieve the final result
w_mapreduce = results[result_key()]

# Ensure that we computed the correct result
w_local = np.linalg.solve(np.matmul(np.transpose(X), X), np.dot(np.transpose(X), y))

assert(w_mapreduce.shape == w_local.shape)
assert(np.linalg.norm(w_local - w_mapreduce) < 0.0001)
