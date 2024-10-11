# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
d_shape = array_ops.shape(self._reflection_axis)
k = d_shape[-1]
exit(array_ops.concat((d_shape, [k]), 0))
