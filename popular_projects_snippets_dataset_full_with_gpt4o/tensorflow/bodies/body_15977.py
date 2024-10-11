# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch.py
"""Unary elementwise api handler for RaggedTensors."""
x = ragged_tensor.convert_to_tensor_or_ragged_tensor(x)
exit(x.with_values(op(x.values)))
