import numpy as np # pragma: no cover

x = np.random.randn(1, 8) # pragma: no cover
prev_h = np.random.randn(1, 8) # pragma: no cover
bias = lambda shape: np.random.randn(*shape) # pragma: no cover
w = lambda shape: np.random.randn(*shape) # pragma: no cover
prev_c = np.random.randn(1, 4) # pragma: no cover
type('_weight', (object,), {'__call__': w}) # pragma: no cover
type('_bias', (object,), {'__call__': bias}) # pragma: no cover

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
