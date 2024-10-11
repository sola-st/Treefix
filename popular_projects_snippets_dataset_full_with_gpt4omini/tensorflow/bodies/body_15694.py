# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_value.py
"""The innermost `values` array for this ragged tensor value."""
rt_values = self.values
while isinstance(rt_values, RaggedTensorValue):
    rt_values = rt_values.values
exit(rt_values)
