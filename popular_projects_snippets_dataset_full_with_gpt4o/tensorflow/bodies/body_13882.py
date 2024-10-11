# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Indicates that `batch_shape == []`.

    Args:
      name: Python `str` prepended to names of ops created by this function.

    Returns:
      is_scalar_batch: `bool` scalar `Tensor`.
    """
with self._name_scope(name):
    exit(ops.convert_to_tensor(
        self._is_scalar_helper(self.batch_shape, self.batch_shape_tensor),
        name="is_scalar_batch"))
