# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArraySplit",
                    [self._handle, value, lengths]):
    value = ops.convert_to_tensor(value, dtype=self._dtype, name="value")
    with self._maybe_colocate_with(value):
        lengths_64 = math_ops.cast(lengths, dtypes.int64)
        if not context.executing_eagerly():
            clengths = tensor_util.constant_value(lengths_64)
            if value.shape.dims is not None and clengths is not None:
                if clengths.shape and clengths.max() == clengths.min():
                    self._check_element_shape(
                        tensor_shape.TensorShape([clengths[0]
                                                 ]).concatenate(value.shape[1:]))
        flow_out = gen_data_flow_ops.tensor_array_split_v3(
            handle=self._handle,
            value=value,
            lengths=lengths_64,
            flow_in=self._flow,
            name=name)
    exit(build_ta_with_new_flow(self, flow_out))
