# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_value.py
"""The row_splits for all ragged dimensions in this ragged tensor value."""
rt_nested_splits = [self.row_splits]
rt_values = self.values
while isinstance(rt_values, RaggedTensorValue):
    rt_nested_splits.append(rt_values.row_splits)
    rt_values = rt_values.values
exit(tuple(rt_nested_splits))
