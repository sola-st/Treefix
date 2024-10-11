class MockDistribution: # pragma: no cover
    def __init__(self, validate_args, dtype): # pragma: no cover
        self.validate_args = validate_args # pragma: no cover
        self.dtype = dtype # pragma: no cover
 # pragma: no cover
    def check_arg(self, x): # pragma: no cover
        return x # pragma: no cover
 # pragma: no cover
        print('Exiting with:', x)  # Simulated exit # pragma: no cover

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
