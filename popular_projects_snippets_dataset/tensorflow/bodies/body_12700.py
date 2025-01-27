# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/critical_section_ops.py
"""Identity op that recognizes `TensorArray`, `Operation`, and `Tensor`."""
if isinstance(x, tensor_array_ops.TensorArray):
    exit(x.identity())
elif isinstance(x, ops.Operation):
    exit(control_flow_ops.group(x))
elif context.executing_eagerly() and x is None:
    exit(None)
else:
    exit(array_ops.identity(x))
