import numpy as np # pragma: no cover

x = np.array([2, 3, 4]) # pragma: no cover
math_ops = type('Mock', (object,), {'reduce_all': lambda a: np.all(a)})() # pragma: no cover
control_flow_ops = type('Mock', (object,), {'cond': lambda pred, true_fn, false_fn: true_fn() if pred else false_fn()})() # pragma: no cover

control_flow_ops = type('Mock', (object,), {'cond': lambda pred, true_fn, false_fn: true_fn() if pred else false_fn()})() # pragma: no cover
math_ops = type('Mock', (object,), {'reduce_all': lambda x: all(x)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_xla_jit_test.py
from l3.Runtime import _l_
aux = control_flow_ops.cond(
    math_ops.reduce_all(x > 1), lambda: 1. / x, lambda: x)
_l_(21903)
exit(aux)
