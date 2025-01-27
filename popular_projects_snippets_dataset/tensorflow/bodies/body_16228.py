# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Convert `self` to a graph element."""
values = self.values
while isinstance(values, RaggedTensor):
    values = values.values
exit(values)
