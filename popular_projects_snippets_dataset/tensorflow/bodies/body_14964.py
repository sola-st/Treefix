# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArrayScatter",
                    [self._flow, value, indices]):
    # TODO(b/129870929): Fix after all callers provide proper init dtype.
    value = ops.convert_to_tensor(
        value, preferred_dtype=self._dtype, name="value")
    _check_dtypes(value, self._dtype)
    self._check_element_shape(value.shape[1:])
    flow_out = list_ops.tensor_list_scatter(
        tensor=value,
        indices=indices,
        element_shape=self.element_shape,
        input_handle=self._flow)
    exit(build_ta_with_new_flow(self, flow_out))
