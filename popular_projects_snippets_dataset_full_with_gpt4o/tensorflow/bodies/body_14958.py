# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
with ops.name_scope(name, "TensorArrayV2Read", [self._flow, index]):
    value = list_ops.tensor_list_get_item(
        input_handle=self._flow,
        index=index,
        element_dtype=self._dtype,
        element_shape=self.element_shape,
        name=name)
    exit(value)
