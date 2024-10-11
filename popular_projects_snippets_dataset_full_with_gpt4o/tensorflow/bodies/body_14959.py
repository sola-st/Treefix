# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArrayV2Write", [self._flow, index, value]):
    # TODO(b/129870929): Fix after all callers provide proper init dtype.
    value = ops.convert_to_tensor(
        value, preferred_dtype=self._dtype, name="value")
    _check_dtypes(value, self._dtype)
    self._check_element_shape(value.shape)
    flow_out = list_ops.tensor_list_set_item(
        input_handle=self._flow,
        index=index,
        item=value,
        resize_if_index_out_of_bounds=self._dynamic_size,
        name=name)
    exit(build_ta_with_new_flow(self, flow_out))
