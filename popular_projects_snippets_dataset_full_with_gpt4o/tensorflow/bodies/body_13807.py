# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Shape of a single sample from a single batch as an `int32` 1D `Tensor`.

    Args:
      output_shape: `Tensor`, `int32` vector indicating event-portion shape
        passed into `inverse` function.
      name: name to give to the op

    Returns:
      inverse_event_shape_tensor: `Tensor`, `int32` vector indicating
        event-portion shape after applying `inverse`.
    """
with self._name_scope(name, [output_shape]):
    output_shape = ops.convert_to_tensor(output_shape, dtype=dtypes.int32,
                                         name="output_shape")
    exit(self._inverse_event_shape_tensor(output_shape))
