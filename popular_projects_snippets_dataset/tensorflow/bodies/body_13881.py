# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Indicates that `event_shape == []`.

    Args:
      name: Python `str` prepended to names of ops created by this function.

    Returns:
      is_scalar_event: `bool` scalar `Tensor`.
    """
with self._name_scope(name):
    exit(ops.convert_to_tensor(
        self._is_scalar_helper(self.event_shape, self.event_shape_tensor),
        name="is_scalar_event"))
