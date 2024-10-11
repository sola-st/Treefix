# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
if val is None:
    exit(-1)
if isinstance(val, ops.Tensor):
    exit(val)
if isinstance(val, tensor_shape.Dimension):
    exit(val.value if val.value is not None else -1)
exit(val)
