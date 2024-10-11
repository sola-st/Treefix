import numpy as np # pragma: no cover

def _bias(shape): return tf.Variable(tf.zeros(shape)) # pragma: no cover
def _weight(shape): return tf.Variable(tf.random.normal(shape)) # pragma: no cover
class MockMathOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def matmul(a, b): return tf.matmul(a, b) # pragma: no cover
    @staticmethod # pragma: no cover
    def sigmoid(x): return tf.sigmoid(x) # pragma: no cover
    @staticmethod # pragma: no cover
    def tanh(x): return tf.tanh(x) # pragma: no cover
class MockArrayOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def concat(values, axis): return tf.concat(values, axis) # pragma: no cover
    @staticmethod # pragma: no cover
    def split(value, num_or_size_splits, axis): return tf.split(value, num_or_size_splits, axis) # pragma: no cover
class MockNN: # pragma: no cover
    @staticmethod # pragma: no cover
    def bias_add(x, bias): return tf.nn.bias_add(x, bias) # pragma: no cover
math_ops = MockMathOps() # pragma: no cover
array_ops = MockArrayOps() # pragma: no cover
nn = MockNN() # pragma: no cover

import numpy as np # pragma: no cover

def _bias(shape): return tf.Variable(tf.zeros(shape), trainable=True) # pragma: no cover
def _weight(shape): return tf.Variable(tf.random.normal(shape, stddev=0.1), trainable=True) # pragma: no cover
class MockMathOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def matmul(a, b): return tf.matmul(a, b) # pragma: no cover
    @staticmethod # pragma: no cover
    def sigmoid(x): return tf.sigmoid(x) # pragma: no cover
    @staticmethod # pragma: no cover
    def tanh(x): return tf.tanh(x) # pragma: no cover
class MockArrayOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def concat(values, axis): return tf.concat(values, axis) # pragma: no cover
    @staticmethod # pragma: no cover
    def split(value, num_or_size_splits, axis): return tf.split(value, num_or_size_splits, axis) # pragma: no cover
class MockNN: # pragma: no cover
    @staticmethod # pragma: no cover
    def bias_add(x, bias): return x + bias # pragma: no cover
math_ops = MockMathOps() # pragma: no cover
array_ops = MockArrayOps() # pragma: no cover
nn = MockNN() # pragma: no cover

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
