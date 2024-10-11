import numpy as np # pragma: no cover

def _bias(shape): return tf.Variable(tf.zeros(shape)) # pragma: no cover
def _weight(shape): return tf.Variable(tf.random.truncated_normal(shape, stddev=0.1)) # pragma: no cover
class MathOps: pass # pragma: no cover
math_ops = MathOps() # pragma: no cover
class ArrayOps: pass # pragma: no cover
array_ops = ArrayOps() # pragma: no cover
class NN: pass # pragma: no cover
nn = NN() # pragma: no cover

import numpy as np # pragma: no cover

class MathOps: pass # pragma: no cover
math_ops = MathOps() # pragma: no cover
class ArrayOps: pass # pragma: no cover
array_ops = ArrayOps() # pragma: no cover
class NN: pass # pragma: no cover
nn = NN() # pragma: no cover

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
