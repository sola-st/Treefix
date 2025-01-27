# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Shape of a single sample from a single batch as a 1-D int32 `Tensor`.

    Args:
      name: name to give to the op

    Returns:
      event_shape: `Tensor`.
    """
with self._name_scope(name):
    if self.event_shape.is_fully_defined():
        exit(ops.convert_to_tensor(self.event_shape.as_list(),
                                     dtype=dtypes.int32,
                                     name="event_shape"))
    exit(self._event_shape_tensor())
