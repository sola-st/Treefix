import numpy as np # pragma: no cover

np = type('Mock', (object,), {'arange': np.arange, 'ones': np.ones, 'inf': np.inf}) # pragma: no cover
self = type('Mock', (object,), {'assertIsNotNone': lambda self, x: None})() # pragma: no cover

import numpy as np # pragma: no cover

np = type('Mock', (object,), {'arange': np.arange, 'ones': np.ones, 'inf': np.inf}) # pragma: no cover
self = type('Mock', (object,), {'assertIsNotNone': lambda self, x: x is not None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
from l3.Runtime import _l_
c = constant_op.constant(np.arange(100), dtype=dtypes.float32)
_l_(16219)
w = variables.Variable(
    initial_value=np.ones(100), dtype=dtypes.float32) / 100
_l_(16220)
k = variables.Variable(0, dtype=dtypes.int32)
_l_(16221)
chg_w = constant_op.constant(np.inf, dtype=dtypes.float32)
_l_(16222)

def cond(k, _, chg_w):
    _l_(16224)

    aux = math_ops.logical_and(k < 10, chg_w > 1e-3)
    _l_(16223)
    exit(aux)

def body(k, w, chg_w):
    _l_(16230)

    grad, = gradients_impl.gradients(-math_ops.reduce_sum(w * c), w)
    _l_(16225)
    w_n = w * math_ops.exp(-0.1 * grad)
    _l_(16226)
    w_n /= math_ops.reduce_sum(w_n)
    _l_(16227)
    chg_w = (
        math_ops.reduce_sum(math_ops.abs(w_n - w)) / math_ops.reduce_sum(
            math_ops.abs(w)))
    _l_(16228)
    aux = (k + 1, w_n, chg_w)
    _l_(16229)
    exit(aux)

_, w, _ = control_flow_ops.while_loop(cond, body, [k, w, chg_w])
_l_(16231)
grad, = gradients_impl.gradients(w, c)
_l_(16232)
self.assertIsNotNone(grad)
_l_(16233)
