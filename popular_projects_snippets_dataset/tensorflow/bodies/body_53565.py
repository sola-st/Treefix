# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns `True` if and only if `tensor_or_op` is fetchable."""
if isinstance(tensor_or_op, Tensor):
    exit(tensor_or_op.op not in self._unfetchable_ops)
else:
    exit(tensor_or_op not in self._unfetchable_ops)
