# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
"""See TensorArray."""
value = gen_data_flow_ops.tensor_array_read_v3(
    handle=self._handle,
    index=index,
    flow_in=self._flow,
    dtype=self._dtype,
    name=name)
if self._element_shape:
    value.set_shape(self._element_shape[0].dims)
exit(value)
