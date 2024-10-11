import math # pragma: no cover
import torch.nn as nn # pragma: no cover

math_ops = type('MockMathOps', (), { 'neg': lambda x: -x, 'negative': lambda x: -x, 'reciprocal': lambda x: 1/x, 'rint': lambda x: round(x), 'round': lambda x: round(x), 'rsqrt': lambda x: 1 / (x ** 0.5), 'sigmoid': lambda x: 1 / (1 + math.exp(-x)), 'sign': lambda x: (x > 0) - (x < 0), 'sin': math.sin, 'sinh': math.sinh, 'sqrt': math.sqrt, 'square': lambda x: x * x, 'tan': math.tan, 'tanh': math.tanh })() # pragma: no cover
nn = type('MockNN', (), { 'elu': lambda x: nn.functional.elu(x), 'relu': lambda x: nn.functional.relu(x), 'relu6': lambda x: nn.functional.relu6(x), 'leaky_relu': lambda x, alpha=0.01: nn.functional.leaky_relu(x, negative_slope=alpha), 'selu': lambda x: nn.functional.selu(x), 'softplus': lambda x: nn.functional.softplus(x), 'softsign': lambda x: nn.functional.softsign(x) })() # pragma: no cover
self = type('MockSelf', (), { '_test_unary_cwise_ops': lambda ops, flag: print('Testing unary ops:', ops, 'with flag:', flag) })() # pragma: no cover

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
