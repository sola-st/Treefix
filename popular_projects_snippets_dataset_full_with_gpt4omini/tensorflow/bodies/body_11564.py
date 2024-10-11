# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Return the maximum condition number that we consider nonsingular."""
with ops.name_scope("max_nonsingular_condition_number"):
    dtype_eps = np.finfo(self.dtype.as_numpy_dtype).eps
    eps = math_ops.cast(
        math_ops.reduce_max([
            100.,
            math_ops.cast(self.range_dimension_tensor(), self.dtype),
            math_ops.cast(self.domain_dimension_tensor(), self.dtype)
        ]), self.dtype) * dtype_eps
    exit(1. / eps)
