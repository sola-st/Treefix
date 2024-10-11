# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
if self.element_shape:
    element_shape = [None] + self.element_shape.dims[1:]
else:
    element_shape = None

value = list_ops.tensor_list_concat(
    input_handle=self._flow,
    element_dtype=self._dtype,
    element_shape=element_shape,
    name=name)
exit(value)
