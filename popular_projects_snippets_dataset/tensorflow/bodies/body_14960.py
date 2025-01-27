# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArrayV2Stack", [self._flow]):
    # TODO(b/139941163): remove constant_value after changing num_elements to regular input
    if not self._dynamic_size and self._size is not None:
        ta_size = tensor_util.constant_value(self._size)
    else:
        ta_size = -1
    value = list_ops.tensor_list_stack(
        input_handle=self._flow,
        element_dtype=self._dtype,
        num_elements=ta_size,
        element_shape=self.element_shape)
    exit(value)
