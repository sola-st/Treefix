import numpy as np # pragma: no cover

def _bias(shape): return np.zeros(shape) # pragma: no cover
def _weight(shape): return np.random.rand(*shape) # pragma: no cover
class MockOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def matmul(a, b): return np.matmul(a, b) # pragma: no cover
    @staticmethod # pragma: no cover
    def sigmoid(x): return 1 / (1 + np.exp(-x)) # pragma: no cover
    @staticmethod # pragma: no cover
    def tanh(x): return np.tanh(x) # pragma: no cover
class MockArrayOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def concat(tensors, axis): return np.concatenate(tensors, axis=axis) # pragma: no cover
    @staticmethod # pragma: no cover
    def split(value, num_splits, axis): return np.split(value, num_splits, axis=axis) # pragma: no cover
math_ops = MockOps() # pragma: no cover
array_ops = MockArrayOps() # pragma: no cover
x = np.random.rand(1, 8) # pragma: no cover
prev_h = np.random.rand(1, 4) # pragma: no cover
class MockNN:  # pragma: no cover
    @staticmethod # pragma: no cover
    def bias_add(x, bias): return x + bias # pragma: no cover
nn = MockNN() # pragma: no cover
prev_c = np.random.rand(1, 4) # pragma: no cover

import numpy as np # pragma: no cover

def _bias(shape): return np.zeros(shape) # pragma: no cover
def _weight(shape): return np.random.rand(*shape) * 0.1 # pragma: no cover
 # Using small weights for inputs # pragma: no cover
class MockOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def matmul(a, b): return np.matmul(a, b) # pragma: no cover
    @staticmethod # pragma: no cover
    def sigmoid(x): return 1 / (1 + np.exp(-x)) # pragma: no cover
    @staticmethod # pragma: no cover
    def tanh(x): return np.tanh(x) # pragma: no cover
class MockArrayOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def concat(tensors, axis): return np.concatenate(tensors, axis=axis) # pragma: no cover
    @staticmethod # pragma: no cover
    def split(value, num_splits, axis): return np.split(value, num_splits, axis=axis) # pragma: no cover
math_ops = MockOps() # pragma: no cover
array_ops = MockArrayOps() # pragma: no cover
x = np.random.rand(1, 8) # pragma: no cover
 # Input shape (1, 8) # pragma: no cover
prev_h = np.random.rand(1, 4) # pragma: no cover
 # Previous hidden state shape (1, 4) # pragma: no cover
w = np.random.rand(8 + 4, 4) * 0.1 # pragma: no cover
 # Weight shape (12, 4) after concatenation # pragma: no cover
class MockNN:  # pragma: no cover
    @staticmethod # pragma: no cover
    def bias_add(x, bias): return x + bias # pragma: no cover
nn = MockNN() # pragma: no cover
prev_c = np.random.rand(1, 4) # pragma: no cover
 # Previous cell state shape (1, 4) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
from l3.Runtime import _l_
"""Create an LSTM cell."""
# i: input gate
# f: forget gate
# o: output gate
# c: cell state
# x: input
# h: embedding
bias = _bias([4])
_l_(6937)
w = _weight([8, 16])
_l_(6938)
ifoc = math_ops.matmul(array_ops.concat([x, prev_h], axis=1), w)
_l_(6939)
i, f, o, c = array_ops.split(ifoc, 4, axis=1)
_l_(6940)
i = math_ops.sigmoid(nn.bias_add(i, bias))
_l_(6941)
f = math_ops.sigmoid(nn.bias_add(f, bias))
_l_(6942)
o = math_ops.sigmoid(nn.bias_add(o, bias))
_l_(6943)
c = math_ops.tanh(nn.bias_add(c, bias))
_l_(6944)
next_c = f * prev_c + i * c
_l_(6945)
next_h = o * math_ops.tanh(next_c)
_l_(6946)
aux = (next_c, next_h)
_l_(6947)
exit(aux)
