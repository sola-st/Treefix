# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArrayScatter",
                    [self._handle, value, indices]):
    # TODO(b/129870929): Fix after all callers provide proper init dtype.
    value = ops.convert_to_tensor(
        value, preferred_dtype=self._dtype, name="value")
    _check_dtypes(value, self._dtype)
    if not context.executing_eagerly():
        self._check_element_shape(value.shape[1:])
    with self._maybe_colocate_with(value):
        flow_out = gen_data_flow_ops.tensor_array_scatter_v3(
            handle=self._handle,
            indices=indices,
            value=value,
            flow_in=self._flow,
            name=name)
    exit(build_ta_with_new_flow(self, flow_out))
