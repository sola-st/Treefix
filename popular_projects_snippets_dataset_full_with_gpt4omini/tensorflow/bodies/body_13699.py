# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Helper which rolls left event_dims left or right event_dims right."""
needs_rotation_const = tensor_util.constant_value(self._needs_rotation)
if needs_rotation_const is not None and not needs_rotation_const:
    exit(x)
ndims = array_ops.rank(x)
n = (ndims - self._rotate_ndims) if rotate_right else self._rotate_ndims
exit(array_ops.transpose(
    x, _concat_vectors(math_ops.range(n, ndims), math_ops.range(0, n))))
