# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
# Condition number for a scalar time identity matrix is one, except when the
# scalar is zero.
exit(array_ops.where_v2(
    math_ops.equal(self._multiplier, 0.),
    math_ops.cast(np.nan, dtype=self.dtype),
    math_ops.cast(1., dtype=self.dtype)))
