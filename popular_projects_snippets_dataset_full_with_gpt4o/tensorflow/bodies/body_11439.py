# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_diag.py
# If d_shape = [5, 3], we return [5, 3, 3].
d_shape = self._diag.shape
exit(d_shape.concatenate(d_shape[-1:]))
