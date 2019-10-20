import numpy as np
from sklearn import datasets

from components.neuralnetwork import *

np.random.seed(0)

X, y = datasets.make_moons(200, noise=0.20)

input_dimensions = 2
num_classes = 2
num_training_examples = len(X)

size_of_hidden_layer = 3
epsilon = 0.01  # learning rate for gradient descent
reg_lambda = 0.01  # regularization strength

network = NeuralNetwork([
    FullyConnectedLayerWithActivation(input_dimensions, size_of_hidden_layer),
    FullyConnectedLayer(size_of_hidden_layer, num_classes),
    SoftMax(num_training_examples)
])

# Train the network with batch gradient descent
for iteration in range(0, 20000):

    # Forward pass
    network.forward(X)
    # Backward pass
    network.backward(y)
    # Parameter updates
    network.update_weights(X, reg_lambda, epsilon)

    if iteration % 1000 == 0:
        print("Loss after iteration %i: %f" % (iteration, calculate_loss(network, X, y)))

assert calculate_loss(network, X, y) < 0.08
