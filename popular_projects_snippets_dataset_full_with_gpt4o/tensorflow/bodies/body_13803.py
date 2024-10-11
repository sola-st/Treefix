# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/bijector_impl.py
"""Shape of a single sample from a single batch as an `int32` 1D `Tensor`.

    Args:
      input_shape: `Tensor`, `int32` vector indicating event-portion shape
        passed into `forward` function.
      name: name to give to the op

    Returns:
      forward_event_shape_tensor: `Tensor`, `int32` vector indicating
        event-portion shape after applying `forward`.
    """
with self._name_scope(name, [input_shape]):
    input_shape = ops.convert_to_tensor(input_shape, dtype=dtypes.int32,
                                        name="input_shape")
    exit(self._forward_event_shape_tensor(input_shape))
