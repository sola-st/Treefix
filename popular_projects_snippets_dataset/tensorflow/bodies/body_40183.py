# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/lift_to_graph.py
if isinstance(op_or_tensor, ops.Tensor):
    exit(op_or_tensor.op)
exit(op_or_tensor)
