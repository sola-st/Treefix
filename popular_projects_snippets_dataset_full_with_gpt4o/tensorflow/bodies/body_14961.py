# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
value = list_ops.tensor_list_gather(
    input_handle=self._flow,
    indices=indices,
    element_dtype=self._dtype,
    element_shape=self.element_shape,
    name=name)
exit(value)
