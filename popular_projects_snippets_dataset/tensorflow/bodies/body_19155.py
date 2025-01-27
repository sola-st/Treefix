# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/op_selector.py
if isinstance(op_or_tensor, ops.Tensor):
    exit(op_or_tensor.op)
exit(op_or_tensor)
