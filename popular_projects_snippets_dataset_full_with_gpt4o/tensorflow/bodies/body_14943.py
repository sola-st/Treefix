# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
if self._element_shape:
    element_shape = self._element_shape[0]
else:
    element_shape = tensor_shape.unknown_shape(None)
value = gen_data_flow_ops.tensor_array_gather_v3(
    handle=self._handle,
    indices=indices,
    flow_in=self._flow,
    dtype=self._dtype,
    name=name,
    element_shape=element_shape)
if self.element_shape:
    value.set_shape([None] + self.element_shape.dims)
exit(value)
