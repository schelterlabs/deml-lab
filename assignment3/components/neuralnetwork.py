import numpy as np


class NeuralNetwork:

    def __init__(self, layers):
        self.layers = layers

    def forward(self, inputs):
        # TODO implement the forward pass through the network
        # TODO each layer must store its output
        # TODO additionally: return the output of the last layer from this function
        pass

    def backward(self, y_true):
        for layer_index in reversed(range(1, len(self.layers))):
            if layer_index == len(self.layers) - 1:
                self.layers[layer_index].backward(y_true, None)
            else:
                previous_gradient = self.layers[layer_index + 1].gradient
                self.layers[layer_index].backward(previous_gradient, self.layers[layer_index - 1].output)

    def update_weights(self, inputs, reg_lambda, epsilon):
        for layer_index in range(0, len(self.layers) - 1):
            if layer_index == 0:
                self.layers[0].update(inputs, self.layers[1].gradient, reg_lambda, epsilon)
            else:
                self.layers[layer_index].update(
                    self.layers[layer_index - 1].output,
                    self.layers[layer_index + 1].gradient,
                    reg_lambda, epsilon)


class FullyConnectedLayer:

    def __init__(self, input_size, layer_size):
        self.W = np.random.randn(input_size, layer_size) / np.sqrt(input_size)
        self.b = np.zeros((1, layer_size))
        self.output = None
        self.gradient = None

    def forward(self, inputs):
        # TODO implement forward pass
        pass

    def backward(self, previous_gradient, inputs):
        self.gradient = previous_gradient.dot(self.W.T) * (1 - np.power(inputs, 2))

    def update(self, inputs, previous_gradient, reg_lambda, epsilon):
        dW = (inputs.T).dot(previous_gradient) + reg_lambda * self.W
        db = np.sum(previous_gradient, axis=0)

        self.W -= epsilon * dW
        self.b -= epsilon * db


class FullyConnectedLayerWithActivation:

    def __init__(self, input_size, layer_size):
        self.W = np.random.randn(input_size, layer_size) / np.sqrt(input_size)
        self.b = np.zeros((1, layer_size))
        self.output = None
        self.gradient = None

    def forward(self, inputs):
        # TODO implement forward pass with tanh as activation function
        pass

    def backward(self, previous_gradient):
        pass

    def update(self, inputs, previous_gradient, reg_lambda, epsilon):
        dW = (inputs.T).dot(previous_gradient) + reg_lambda * self.W
        db = np.sum(previous_gradient, axis=0)

        self.W -= epsilon * dW
        self.b -= epsilon * db


class SoftMax:

    def __init__(self, num_examples):
        self.output = None
        self.gradient = None
        self.num_examples = num_examples

    def forward(self, inputs):
        # TODO implement softmax computation
        pass

    def backward(self, y_true, inputs):
        self.gradient = np.copy(self.output)
        self.gradient[range(self.num_examples), y_true] -= 1


# Helper function to evaluate the total loss on the dataset
def calculate_loss(network, X, y):
    num_examples = len(X)
    probabilities = network.forward(X)
    return (1.0 / num_examples) * np.sum(-np.log(probabilities[range(num_examples), y]))


def predict(network, x):
    probabilities = network.forward(x)
    return np.argmax(probabilities, axis=1)
