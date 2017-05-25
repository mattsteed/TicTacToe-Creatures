# Matthew Steed
# Code for neural network

import numpy as np
from scipy.misc import logsumexp
from copy import copy



# Definition of a hidden layer of weights and biases for neural net
class HiddenLayer:
  def __init__(self, in_size, out_size):
    self.in_size = in_size
    self.out_size = out_size

    # This is the Xavier initialization r
    r = np.sqrt(3.0 / in_size)

    # The uniform function gives matrices in the input shapes with random weights
    # in [-r, r].
    self._weights = np.random.uniform(-r, r, (in_size, out_size))
    self._bias = np.random.uniform(-r, r, (1, out_size))

    # These are the accumulated gradients for rmsprop
    self._wr = np.zeros((in_size, out_size))
    self._br = np.zeros((1, out_size))

  def forward(self, input):
    """
    Suppose there are N samples of dimension d that are being input.
    Note that d is the self.in_size parameter.
    input: N x d numpy array of the input samples 

    output: N x self.out_size numpy array of the output result for each input
    """
    self._input = copy(input)
    self._output = np.dot(self._input, self._weights) + self._bias
    return self._output
  
  def back_prop(self, grad_out, eta, weight_decay=0):
    """
    Suppose there are N samples of dimension d that were input.
    Note that d is the self.in_size parameter.
    grad_out: N x out_size numpy array of the gradient of the loss wrt the 
              output of the layer 
    eta: Learning rate for gradient descent
    weight_decay: the weight_decay parameter

    grad_input: N x d numpy array of the gradient of the input that will be 
                passed back for backprop
    """
    N = self._input.shape[0]
    grad_weights = (1.0 / N) * np.dot(self._input.T, grad_out)
    grad_bias = np.mean(grad_out, axis=0)
    grad_input = np.dot(grad_out, self._weights.T)
    
    # Update weights and biases
    self._weights = self._weights - eta * (grad_weights + weight_decay * self._weights)
    self._bias = self._bias - eta * (grad_bias + weight_decay * self._bias)

    return grad_input


  def rmsprop(self, grad_out, eta, delta, rho, weight_decay=0):
    """
    N samples of dimension d that are input.
    Note that d is the self.in_size parameter.
    grad_out: N x out_size numpy array of the gradient of the loss wrt the 
              output of the layer 
    eta: Learning rate for gradient descent
    delta, rho: RMSProp parameters
    weight_decay: the weight_decay parameter

    grad_input: N x d numpy array of the gradient of the input that will be 
                passed back for backprop
    """
    N = self._input.shape[0]
    grad_weights = (1.0 / N) * np.dot(self._input.T, grad_out)
    grad_bias = np.mean(grad_out, axis=0)
    grad_input = np.dot(grad_out, self._weights.T)

    # Accumulate the gradients
    self._wr = rho * self._wr + (1-rho) * (grad_weights * grad_weights)
    self._br = rho * self._br + (1-rho) * (grad_bias * grad_bias)

    # Compute the weight updates
    weight_update = -eta * 1/(delta + np.sqrt(self._wr)) * grad_weights
    bias_update = -eta * 1/(delta + np.sqrt(self._br)) * grad_bias
    
    # Update weights and biases
    self._weights = self._weights + weight_update - eta*weight_decay*self._weights
    self._bias = self._bias + bias_update - eta*weight_decay*self._bias

    return grad_input
 
  def set_mode(self, mode):
    """
    This is for dropout, not used here.
    """
    return
 

# Definition of tanh activation layer for neural net
class TanhLayer:
  def __init__(self):
    return

  def forward(self, input):
    """
    Suppose there are N samples of dimension d that are being input.
    input: N x d numpy array of the input samples 

    output: N x d numpy array of tanh applied element-wise
    """
    self._input = copy(input)
    return np.tanh(self._input)

  def back_prop(self, grad_out, eta, weight_decay=0):
    """
    Suppose there are N samples of dimension d that were input.
    grad_out: N x d numpy array of the gradient of the loss wrt the 
              output of the layer 
    eta: Learning rate for gradient descent. It is not used here, but it is an
         argument that is passed in to every layer for backprop
    weight_decay: Weight decay parameter. Not used here.

    grad_input: N x d numpy array of the gradient of the input that will be 
                passed back for backprop
    """
    grad_input = grad_out * (1 - np.square(np.tanh(self._input)))
    return grad_input

  def rmsprop(self, grad_out, eta, delta, rho, weight_decay=0):
    """
    This is the same as back_prop for layers with no parameters
    """
    grad_input = grad_out * (1 - np.square(np.tanh(self._input)))
    return grad_input

  def set_mode(self, mode):
    """
    This is for dropout, not used here.
    """
    return
 

# Definition of ReLU activation layer for neural net
class ReluLayer:
  def __init__(self):
    return

  def forward(self, input):
    """
    Suppose there are N samples of dimension d that are being input.
    input: N x d numpy array of the input samples 

    output: N x d numpy array of max(0,x) applied element-wise
    """
    self._input = copy(input)
    return np.maximum(self._input, 0)

  def back_prop(self, grad_out, eta, weight_decay=0):
    """
    Suppose there are N samples of dimension d that were input.
    grad_out: N x d numpy array of the gradient of the loss wrt the 
              output of the layer 
    eta: Learning rate for gradient descent. It is not used here, but it is an
         argument that is passed in to every layer for backprop
    weight_decay: Weight decay parameter. Not used here.

    grad_input: N x d numpy array of the gradient of the input that will be 
                passed back for backprop
    """
    grad_input = grad_out * (self._input > 0)
    return grad_input

  def rmsprop(self, grad_out, eta, delta, rho, weight_decay=0):
    """
    This is the same as back_prop for layers with no parameters
    """
    grad_input = grad_out * (self._input > 0)
    return grad_input

  def set_mode(self, mode):
    """
    This is for dropout, not used here.
    """
    return
 

# Definition of Dropout layer for training
class Dropout:
  def __init__(self, parameter):
    """
    in_size: The size of the vector that will be fed in
    parameter: Bernoulli parameter that describes how much dropout there is
    """
    self._p = parameter

  def forward(self, input):
    """
    Suppose there are N samples of dimension d that are being input.
    input: N x d numpy array of the input samples 

    output: N x d numpy array with some things zeroed out
    """
    self._input = copy(input)
    d = input.shape[1]
    if (self._mode == 'train'):
      self._mask = np.random.binomial(1, self._p, (1, d))
    else:
      self._mask = self._p * np.ones((1, d))
    return input * self._mask

  def back_prop(self, grad_out, eta, weight_decay=0):
    """
    Suppose there are N samples of dimension d that were input.
    grad_out: N x d numpy array of the gradient of the loss wrt the 
              output of the layer 
    eta: Learning rate for gradient descent. It is not used here, but it is an
         argument that is passed in to every layer for backprop
    weight_decay: Weight decay parameter. Not used here.

    grad_input: N x d numpy array of the gradient of the input that will be 
                passed back for backprop
    """
    grad_input = grad_out * self._mask
    return grad_input

  def rmsprop(self, grad_out, eta, delta, rho, weight_decay=0):
    """
    This is the same as back_prop for layers with no parameters
    """
    grad_input = grad_out * self._mask
    return grad_input

  def set_mode(self, mode):
    """
    mode: This is the mode for the dopout layer. If it is the string 'train',
        the layer will be in training mode. For anything else, the layer
        will be in prediction mode.
    """
    self._mode = mode


# Definition of softmax layer for neural net
# This layer has built-in cross-entropy loss between activations and one-hot labels
# This layer returns the crossentropy loss rather than softmax activations
# Note: If you want actual softmax activations, stop just before this layer and apply
#       the softmax function to that output
class SoftmaxLayer:
  def __init__(self):
    pass

  def forward(self, input, labels):
    """
    Suppose there are N samples being input and C classes.
    input: N x C numpy array of the input class activations 
    labels: N x C one-hot vectors giving the classes of the input samples

    output: average of cross-entropy losses between labels and softmax of input
    """
    self._input = copy(input)
    loss = np.mean(np.sum(-self._input * labels, axis=1) + logsumexp(self._input, axis=1))
    return loss 

  def back_prop(self, labels):
    """
    Suppose there are N being input and C classes. 
    labels: N x C one-hot vectors giving the classes of the input samples

    grad_input: N x C numpy array of the gradient of the input that will be 
                passed back for backprop
    """
    N = self._input.shape[0]
    grad_input = np.exp(self._input)
    grad_input = grad_input / np.sum(grad_input, axis=1).reshape(N, 1)
    grad_input = grad_input - labels
    return grad_input


# Definition of squared loss layer for neural net
# This layer returns the squared loss given a predicted vector and a label
class SquaredLoss:
  def __init__(self):
    pass

  def forward(self, predictions, labels):
    """
    predictions: N x C numpy array of the input class activations 
    labels: N x C array that the input should match

    output: average square loss on the whole input sample
    """
    self._input = copy(predictions)
    loss = np.mean(np.sum(np.square(predictions - labels), axis=1))
    return loss

  def back_prop(self, labels):
    N = self._input.shape[0]
    grad_input = 2.0 / N * (self._input - labels)
    return grad_input



# Definition of Neural Net class
class NeuralNet:
  def __init__(self):
    self._layers = []
    self._size = 0
    return

  def add_layer(self, layer):
    self._layers.append(layer)
    self._size += 1
    return

  def forward(self, input):
    #self._output = copy(input)    
    self._output = input    
    for layer in self._layers:
      self._output = layer.forward(self._output)
    return self._output

  def back_prop(self, grad_out, eta, weight_decay=0):
    for i in range(self._size, 0, -1):
      layer = self._layers[i-1]
      grad_out = layer.back_prop(grad_out, eta, weight_decay)
    return

  def rmsprop(self, grad_out, eta, delta, rho, weight_decay=0):
    for i in range(self._size, 0, -1):
      layer = self._layers[i-1]
      grad_out = layer.rmsprop(grad_out, eta, delta, rho, weight_decay)
    return

  def set_mode(self, mode):
    """
    This sets the mode for dropout. It should be 'train' for training.
    It can be anything else for prediction.
    """
    for layer in self._layers:
      layer.set_mode(mode)
    return
 
