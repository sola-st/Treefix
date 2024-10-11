# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
perm_shape = array_ops.shape(self._perm)
k = perm_shape[-1]
exit(array_ops.concat((perm_shape, [k]), 0))
