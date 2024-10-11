# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
if isinstance(maybe_ta, tensor_array_ops.TensorArray):
    exit(maybe_ta.flow)
exit(maybe_ta)
