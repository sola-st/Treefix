import numpy as np # pragma: no cover

x = np.array([0.5, 0.5]) # pragma: no cover
control_flow_ops = type('Mock', (object,), {'with_dependencies': lambda deps, x: x})() # pragma: no cover
check_ops = type('Mock', (object,), {'assert_positive': lambda x, message: True, 'assert_near': lambda a, b, message: True})() # pragma: no cover
array_ops = type('Mock', (object,), {'ones': lambda shape, dtype: np.ones(shape, dtype=dtype)})() # pragma: no cover
math_ops = type('Mock', (object,), {'reduce_sum': lambda x, axis: np.sum(x)})() # pragma: no cover
self = type('Mock', (object,), {'validate_args': False, 'dtype': np.float32})() # pragma: no cover

class MockSelf(object): # pragma: no cover
    validate_args = False # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
from l3.Runtime import _l_
"""Checks the validity of a sample."""
if not self.validate_args:
    _l_(19188)

    aux = x
    _l_(19187)
    exit(aux)
aux = control_flow_ops.with_dependencies([
    check_ops.assert_positive(x, message="samples must be positive"),
    check_ops.assert_near(
        array_ops.ones([], dtype=self.dtype),
        math_ops.reduce_sum(x, -1),
        message="sample last-dimension must sum to `1`"),
], x)
_l_(19189)
exit(aux)
