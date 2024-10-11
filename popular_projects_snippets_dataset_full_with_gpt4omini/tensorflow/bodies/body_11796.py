# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_lower_triangular.py
"""Gets the `tril` kwarg, with upper part zero-d out."""
exit(array_ops.matrix_band_part(self._tril, -1, 0))
