# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
from l3.Runtime import _l_
real_ops = [
    math_ops.neg,
    math_ops.negative,
    math_ops.reciprocal,
    math_ops.rint,
    math_ops.round,
    math_ops.rsqrt,
    math_ops.sigmoid,
    math_ops.sign,
    math_ops.sin,
    math_ops.sinh,
    math_ops.sqrt,
    math_ops.square,
    math_ops.tan,
    math_ops.tanh,
    nn.elu,
    nn.relu,
    nn.relu6,
    lambda t: nn.leaky_relu(t, alpha=0.1),
    nn.selu,
    nn.softplus,
    nn.softsign,
]
_l_(9899)
self._test_unary_cwise_ops(real_ops, False)
_l_(9900)
