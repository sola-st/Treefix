# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Private default implementation of _assert_non_singular."""
logging.warn(
    "Using (possibly slow) default implementation of assert_non_singular."
    "  Requires conversion to a dense matrix and O(N^3) operations.")
if self._can_use_cholesky():
    exit(self.assert_positive_definite())
else:
    singular_values = linalg_ops.svd(self.to_dense(), compute_uv=False)
    # TODO(langmore) Add .eig and .cond as methods.
    cond = (math_ops.reduce_max(singular_values, axis=-1) /
            math_ops.reduce_min(singular_values, axis=-1))
    exit(check_ops.assert_less(
        cond,
        self._max_condition_number_to_be_non_singular(),
        message="Singular matrix up to precision epsilon."))
