## Task 1: Implementing Layers in a Neural Network

The goal of this [task](task1.py) is to complete the implementation of a neural network for classifying points from a synthetically generated dataset:

![](moon.png)

You only have to implement the forward pass; the backward pass and weight updates are already given. The network is defined as follows:  

![](network.png)

Implement the forward pass in the [first fully connected layer, which applies a `tanh` non-linearity](components/neuralnetwork.py#L65), in the [second fully connected layer](components/neuralnetwork.py#L42) and in the [softmax output](components/neuralnetwork.py#L87). Finally, invoke your implemented methods to conduct the [full forward pass through the network](components/neuralnetwork.py#L9) and return the computed probabilities. You can execute this task via `python task1.py`

## Task 2, 3 & 4: Translating Scikit-learn Pipelines to Dataflow Graphs

In the remaining three tasks, you have to implement [a method to convert scikit-learn pipelines into a dataflow representation](components/graph.py#L48). Given a pipeline, your code has to inspect it and generate a list of connected [DataflowVertex](components/graph.py#L1) objects, which represent the operations and dataflow in the pipeline.

A vertex in this graph is defined as follows, where the `name` refers to the step name in the pipeline, the `operation` is the name of the transformer class which executes the step and the `parent_vertices` are operations that the current vertex depends on.

```python
class DataFlowVertex:
    def __init__(self, parent_vertices, name, operation):
        self.parent_vertices = parent_vertices
        self.name = name
        self.operation = operation
```
Your method has to handle four different pipelines with growing complexity. The resulting graphs should look as follows:

![](graphs.png)
