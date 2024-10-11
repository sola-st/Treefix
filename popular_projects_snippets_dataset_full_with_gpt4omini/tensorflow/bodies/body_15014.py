# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
if not isinstance(value, TensorArray):
    raise TypeError("Expected value to be a TensorArray, but got: `{}`".format(
        type(value)))
if value.flow is not None and value.flow.dtype == dtypes.variant:
    exit([value.flow])
else:
    # Convert to a TF2-style TensorArray.
    # TODO(ebrevdo): Add an "_as_variant" method to TensorArray class, or
    # "implementation / as_variant" arg to TensorArray constructor.
    with ops.name_scope("convert_tensor_array"):
        flow = list_ops.tensor_list_from_tensor(
            tensor=value.stack(), element_shape=value.element_shape)
    exit([flow])
