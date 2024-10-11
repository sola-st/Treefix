import numpy as np # pragma: no cover

_bias = lambda shape: tf.zeros(shape, dtype=tf.float32) # pragma: no cover
_weight = lambda shape: tf.random.uniform(shape, minval=-1, maxval=1, dtype=tf.float32) # pragma: no cover

import numpy as np # pragma: no cover

_bias = lambda shape: np.zeros(shape, dtype=np.float32) # pragma: no cover
_weight = lambda shape: np.random.uniform(low=-1, high=1, size=shape).astype(np.float32) # pragma: no cover
math_ops = type('Mock', (object,), {'matmul': lambda a, b: np.dot(a, b), 'sigmoid': lambda x: 1 / (1 + np.exp(-x)), 'tanh': np.tanh})() # pragma: no cover
array_ops = type('Mock', (object,), {'concat': np.concatenate, 'split': lambda x, num, axis: np.array_split(x, num, axis)})() # pragma: no cover
nn = type('Mock', (object,), {'bias_add': np.add})() # pragma: no cover
x = np.random.uniform(low=-1, high=1, size=(1, 8)).astype(np.float32) # pragma: no cover
prev_h = np.random.uniform(low=-1, high=1, size=(1, 8)).astype(np.float32) # pragma: no cover
prev_c = np.random.uniform(low=-1, high=1, size=(1, 4)).astype(np.float32) # pragma: no cover

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
_l_(19626)
w = _weight([8, 16])
_l_(19627)
ifoc = math_ops.matmul(array_ops.concat([x, prev_h], axis=1), w)
_l_(19628)
i, f, o, c = array_ops.split(ifoc, 4, axis=1)
_l_(19629)
i = math_ops.sigmoid(nn.bias_add(i, bias))
_l_(19630)
f = math_ops.sigmoid(nn.bias_add(f, bias))
_l_(19631)
o = math_ops.sigmoid(nn.bias_add(o, bias))
_l_(19632)
c = math_ops.tanh(nn.bias_add(c, bias))
_l_(19633)
next_c = f * prev_c + i * c
_l_(19634)
next_h = o * math_ops.tanh(next_c)
_l_(19635)
aux = (next_c, next_h)
_l_(19636)
exit(aux)
