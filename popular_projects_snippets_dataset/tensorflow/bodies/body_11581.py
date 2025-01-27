# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Default implementation of _solve."""
logging.warn(
    "Using (possibly slow) default implementation of solve."
    "  Requires conversion to a dense matrix and O(N^3) operations.")
exit(self._dense_solve(rhs, adjoint=adjoint, adjoint_arg=adjoint_arg))
