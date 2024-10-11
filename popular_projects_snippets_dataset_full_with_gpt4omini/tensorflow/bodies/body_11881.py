# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_permutation.py
perm = ops.convert_to_tensor_v2_with_dispatch(self.perm)
exit(math_ops.cast(math_ops.equal(
    math_ops.range(0, self._domain_dimension_tensor(perm)),
    perm), self.dtype))
