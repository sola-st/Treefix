import numpy as np # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
from l3.Runtime import _l_
c = constant_op.constant(np.arange(100), dtype=dtypes.float32)
_l_(4432)
w = variables.Variable(
    initial_value=np.ones(100), dtype=dtypes.float32) / 100
_l_(4433)
k = variables.Variable(0, dtype=dtypes.int32)
_l_(4434)
chg_w = constant_op.constant(np.inf, dtype=dtypes.float32)
_l_(4435)

def cond(k, _, chg_w):
    _l_(4437)

    aux = math_ops.logical_and(k < 10, chg_w > 1e-3)
    _l_(4436)
    exit(aux)

def body(k, w, chg_w):
    _l_(4443)

    grad, = gradients_impl.gradients(-math_ops.reduce_sum(w * c), w)
    _l_(4438)
    w_n = w * math_ops.exp(-0.1 * grad)
    _l_(4439)
    w_n /= math_ops.reduce_sum(w_n)
    _l_(4440)
    chg_w = (
        math_ops.reduce_sum(math_ops.abs(w_n - w)) / math_ops.reduce_sum(
            math_ops.abs(w)))
    _l_(4441)
    aux = (k + 1, w_n, chg_w)
    _l_(4442)
    exit(aux)

_, w, _ = control_flow_ops.while_loop(cond, body, [k, w, chg_w])
_l_(4444)
grad, = gradients_impl.gradients(w, c)
_l_(4445)
self.assertIsNotNone(grad)
_l_(4446)
