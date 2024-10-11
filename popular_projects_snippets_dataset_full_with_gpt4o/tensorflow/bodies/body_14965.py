# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArraySplit", [self._flow, value, lengths]):
    # TODO(b/129870929): Fix after all callers provide proper init dtype.
    value = ops.convert_to_tensor(
        value, preferred_dtype=self._dtype, name="value")
    _check_dtypes(value, self._dtype)
    lengths_64 = math_ops.cast(lengths, dtypes.int64)
    if not context.executing_eagerly():
        clengths = tensor_util.constant_value(lengths_64)
        if value.shape.dims is not None and clengths is not None:
            if clengths.shape and clengths.max() == clengths.min():
                self._check_element_shape(
                    tensor_shape.TensorShape([clengths[0]
                                             ]).concatenate(value.shape[1:]))
    flow_out = list_ops.tensor_list_split(
        tensor=value,
        lengths=lengths_64,
        element_shape=self.element_shape,
        name=name)
    exit(build_ta_with_new_flow(self, flow_out))
