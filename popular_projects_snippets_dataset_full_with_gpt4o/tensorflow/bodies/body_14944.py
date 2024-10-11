# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
value, _ = gen_data_flow_ops.tensor_array_concat_v3(
    handle=self._handle,
    flow_in=self._flow,
    dtype=self._dtype,
    name=name,
    element_shape_except0=self.element_shape[1:])
if self.element_shape:
    value.set_shape([None] + self.element_shape.dims[1:])
exit(value)
