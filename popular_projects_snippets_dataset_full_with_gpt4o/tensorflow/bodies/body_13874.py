# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Shape of a single sample from a single event index as a 1-D `Tensor`.

    The batch dimensions are indexes into independent, non-identical
    parameterizations of this distribution.

    Args:
      name: name to give to the op

    Returns:
      batch_shape: `Tensor`.
    """
with self._name_scope(name):
    if self.batch_shape.is_fully_defined():
        exit(ops.convert_to_tensor(self.batch_shape.as_list(),
                                     dtype=dtypes.int32,
                                     name="batch_shape"))
    exit(self._batch_shape_tensor())
