import numpy as np # pragma: no cover

math_ops = type("MockMathOps", (object,), { "neg": np.negative, "negative": np.negative, "reciprocal": np.reciprocal, "rint": np.rint, "round": np.round, "rsqrt": lambda x: 1 / np.sqrt(x), "sigmoid": lambda x: 1 / (1 + np.exp(-x)), "sign": np.sign, "sin": np.sin, "sinh": np.sinh, "sqrt": np.sqrt, "square": np.square, "tan": np.tan, "tanh": np.tanh })() # pragma: no cover
nn = type("MockNN", (object,), { "elu": lambda x: np.where(x > 0, x, np.exp(x) - 1), "relu": lambda x: np.maximum(0, x), "relu6": lambda x: np.minimum(np.maximum(0, x), 6), "leaky_relu": lambda t, alpha=0.1: np.where(t > 0, t, t * alpha), "selu": lambda x: x if x > 0 else 1.67326 * (np.exp(x) - 1), "softplus": lambda x: np.log(1 + np.exp(x)), "softsign": lambda x: x / (1 + np.abs(x)) })() # pragma: no cover
self = type("SelfMock", (object,), { "_test_unary_cwise_ops": lambda self, ops, flag: None })() # pragma: no cover

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
_l_(22175)
self._test_unary_cwise_ops(real_ops, False)
_l_(22176)
