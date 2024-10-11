# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
if not isinstance(value, TensorArray):
    raise TypeError("Expected value to be a TensorArray, but got: `{}`".format(
        type(value)))

exit(TensorArraySpec(
    dtype=value.dtype,
    element_shape=value.element_shape,
    dynamic_size=value.dynamic_size,
    infer_shape=value._infer_shape))  # pylint: disable=protected-access
