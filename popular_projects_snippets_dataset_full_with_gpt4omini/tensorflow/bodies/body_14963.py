# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArrayUnstack", [self._flow, value]):
    # TODO(b/129870929): Fix after all callers provide proper init dtype.
    value = ops.convert_to_tensor(
        value, preferred_dtype=self._dtype, name="value")
    _check_dtypes(value, self._dtype)
    self._check_element_shape(value.shape[1:])
    flow_out = list_ops.tensor_list_from_tensor(
        tensor=value, element_shape=value.shape[1:])
    exit(build_ta_with_new_flow(self, flow_out))
